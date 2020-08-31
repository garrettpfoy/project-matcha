from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
import gspread

##SETTINGS! DO NOT CHANGE UNLESS INSTRUCTED

#Root Directory, do not include individual file names, path should end with \src
ROOT_DIRECTORY = r"C:\Users\gfoy\Documents\Complete\src"
REGISTER_NAME = "Garrett"

##Google Sheet Key (Must match format [CB_Asset, HS_Asset, MAC, SSID, Password, Status])
SHEET_KEY = '1JFT6_3Jz-IA9jMFV2XtYWjHJx9shnq-gAhgb-B9XR-k'

REGISTER_KEY = '18VHRgCU2FIwYCkXBmLXc2QKSbCOXff0mw6DMpC1b8tA'

##What sheet should we pull data from?
WORKSHEET_PULL_NAME = "Data"

##Should we output the finalized pairing to a seperate worksheet?
WORKSHEET_PUSH = True

##What sheet should we push paired sets to?
WORKSHEET_PUSH_NAME = "Completed"

##What index in the sheet array should we pull Chromebook Asset tags from?
CB_ASSET_INDEX  = 0

##What index in the sheet array should we pull Chromebook Serial Tags from?
CB_SERIAL_INDEX = 1

##What index in the sheet array should we pull Hotspot Asset tags from?
HS_ASSET_INDEX = 3

##What index in the sheet array should we pull MAC addresses from?
MAC_ADDRESS_INDEX = 2

##What index in the sheet array should we pull SSID names from?
SSID_INDEX = 4

##What index in the sheet array should we pull hotspot passwords from?
PASSWORD_INDEX = 5

##What index in the sheet array should we push status upgrades to?
STATUS_INDEX = 6

##What file should we configure the SheetsAPI service bot? (JSON is quickest) (should be in root directory)
SERVICE_BOT = r"\service_bot.json"

##How long (in seconds) should we wait before interacting with a page after a load?
WEBPAGE_LOAD_TIME = 1

##How long should we allow the script to search for an element to interact with (in seconds)?
IMPLICIT_WAIT = 0.25

##How long should we wait for other misc tasks (in seconds)?
OTHER_WAIT = 0.75

##What password should we first try to log in with?
LIKELY_PASSWORD = "5gT8at4x"

##What backup password should we attempt to log in with?
UNLIKELY_PASSWORD = "admin"

##If the password is UNLIKELY_PASSWORD, should we change it to be LIKELY_PASSWORD ?
FIX_PASSWORD = True

REGISTER = True

##Takes in the asset number (assumably from scanner)
assetNumber = input("Please scan the asset tag of the chromebook: ")

if(REGISTER):
    serialNumber = input("Please scan the serial number of the chromebook: ")

hotspotAsset = input("Please scan the asset tag of the hotspot: ")

if(REGISTER):
    studentID = input("Please enter the student ID tag: ")

##In order to run a similar script on multiple accounts, we must connect to Google's Service Bot API
##(in this case it is used for SheetsAPI)
##If you want to look into the details, look into the service_bot.json package.
gc = gspread.service_account(filename=ROOT_DIRECTORY + SERVICE_BOT)
macAddresses = gc.open_by_key(SHEET_KEY)

registry = gc.open_by_key(REGISTER_KEY)

##Once we have an instance of the bot, we can load in the worksheet
##and find the value we want (and the row it is in)
worksheet = macAddresses.worksheet(WORKSHEET_PULL_NAME)
assetCell = worksheet.find(assetNumber)
assetRow = worksheet.row_values(assetCell.row)

registrySheet = registry.worksheet(REGISTER_NAME)

##For the sheet this script was built, the chromebook and hotspot are not automatically paired
##So we must scan both the hotspot, and the chromebook's asset tags
hotspotCell = worksheet.find(hotspotAsset)
hotspotRow = worksheet.row_values(hotspotCell.row)

##Start to log what the script is doing in real-time
worksheet.update_cell(assetCell.row, (STATUS_INDEX + 1), "Running...")

##Once we have the row, we can pull as much info we want as an array,
##such as MAC, wifi SSID, and the wifi password.
macAddress = assetRow[MAC_ADDRESS_INDEX]
wifiName = hotspotRow[SSID_INDEX]
wifiPassword = hotspotRow[PASSWORD_INDEX]

##Printing out passwords in the logs to help possibly debug index values
print("Successfully connected to Google Sheets, gathering values...")
print("Pulled MAC... " + macAddress)
print("Pulled SSID..." + wifiName)
print("Pulled password..." + wifiPassword)

##Used to tell whether or not we log in using the backup password, we set it to False
##for now to insure we don't waste time later in the script.
unlikelyPassword = False

##Using selenium to work with Chrome as it is the most robust python
##web scriptor out their (and most optimised)
##As of latest selenium update, the chromedriver.exe is no longer needed, however keeping
##it is not a poor choice.
driver = webdriver.Chrome()
driver.get("http://192.168.0.1/")

##Sleeping to give webpage time to load
time.sleep(WEBPAGE_LOAD_TIME)

##Locating password box and inputing the "main" password

##I will heavily document this process so you can reference this one
##Due to the nature of Seleneium, and the dangerous task of finding
##an element, it is important to use a try/catch to ensure errors
##are readable and are optimized
try:
    ##Selenium offers an implicitly_wait method to tell the next find_element method to have a certain
    ##amount of time to find the element before moving on/erroring out. In this case, the implicit wait
    ##is attached to the passwordBox's find_element. This is useful if you want to allow the script to anticipate
    ##a page load, without having to worry about exessive delay as it doesn't have to reach the max time. (eg. if you put 10 here, as soon as it loads it would move on)
    driver.implicitly_wait(1)

    ##Finding elements is a difficult process as the webpage is dynamic and often times changes absolute xpath's as you see below. If possible, use a broad argument
    ##such as //input or //button, or a find_element_by_css_selector, HOWEVER this does not always work. To find these elements, first go to the webpage, inspect element, then right Click
    ##the element you are targeting and click inspect element once again, this should bring you to the exact element in the HTML code. Right-click the highlighted code, and press COPY --> Copy Full Xpath
    ##If this doesn't work, I would recommend getting the SeleniumIDE extension on chrome and finding the element locator from there.
    passwordBox = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[1]/form/div[1]/div/div/input")

    ##Whenever we want to input text, it is smart to click the element to insure the webpage is ready for text input
    passwordBox.click()

    ##Whenever you want to input text, the best way is to just send the keys, in this case, we send the likely password into the input box
    passwordBox.send_keys(LIKELY_PASSWORD)

    ##You can either press the box, or press enter if applicable, in this case it is easier, and more efficient to press enter once the password is
    ##REMEMEBER: Python (without await) is syncrounous, meaning you don't have to worry about pressing enter before the password has been typed!
    passwordBox.send_keys(Keys.ENTER)

    ##Throughout the process whenever you enter something or are expecting a page to load, you want to sleep just to give the connection some time to make
    ##contact.
    time.sleep(1)
except:
    ##Every exception should have an error code unique to it's part in the code, and be short and sweet.
    ##Typically you want to organize it by page, area, and action. In this case it is the initial page, password section, and entry action that would fail
    print("Task failed at process: INITIAL_PASSWORD_ENTRY")

    ##Optional: Here we update the google sheet with the error code presented so if you miss the error in console, you can view it elsewhere
    worksheet.update_cell(assetCell.row, (STATUS_INDEX + 1), "INITIAL_PASSWORD_ENTRY")

    ##Here we quit out of the Selenium driver, which is basically just the instance of chrome
    driver.quit()

    ##Lastly, we quit out of the program as if this errors out, we don't want any false-successes in the code, and should alert the user of the error
    ##rather then risking it kinda working out.
    exit()

try:
    driver.implicitly_wait(1)
    passwordFailCheck = driver.find_element_by_xpath("//span[contains(.,'OK')]")
    if(passwordFailCheck.is_displayed()):
        passwordFailCheck.click()

    try:
        passwordBoxTwo = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[1]/form/div[1]/div/div/input")
        passwordBoxTwo.click()
        passwordBoxTwo.clear()
        passwordBoxTwo.send_keys(UNLIKELY_PASSWORD)
        passwordBoxTwo.send_keys(Keys.ENTER)

        unlikelyPassword = True

        time.sleep(1)
    except:
        print("Task failed at process INITIAL_PASSWORD_ENTRY_UNLIKEY")
        driver.quit()
        exit()
except:
    print("Password " + LIKELY_PASSWORD + " was accepted")

isOffline = True

while(isOffline):
    driver.implicitly_wait(IMPLICIT_WAIT)
    connectionStatus = driver.find_element_by_xpath("/html/body/div[1]/section/header[1]/div/div[3]/ul/li[4]/span")
    if(connectionStatus.is_displayed()):
        isOffline = False
    else:
        print("Task raised an exception at process: CHECK_CONNECTION_STATUS")
        print("This almost always means the webpage is lagging, we will try to connect again momentarily")
        time.sleep(OTHER_WAIT)


##We are now at the home page, time to navigate to the settings tab
##Navigating to the WifiSetings portion of the process
try:
    driver.implicitly_wait(IMPLICIT_WAIT)
    settingsButton = driver.find_element_by_xpath("/html/body/div/section/header[2]/ul/li[4]")
    settingsButton.click()
    print("Successfully navigated to WifiSettings! Moving on...")
except:
    print("Task failed at process: NAVIGATE_SETTINGS_BAR")
    worksheet.update_cell(assetCell.row, (STATUS_INDEX + 1), "NAVIGATE_SETTINGS_BAR")
    driver.quit()
    exit()

time.sleep(WEBPAGE_LOAD_TIME)

##We are now at the wifi settings page, time to set the name and the password
try:
    driver.implicitly_wait(IMPLICIT_WAIT)
    nameBox = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div[2]/div[2]/div/form/div[1]/div/div/input")
    nameBox.clear()
    nameBox.send_keys(wifiName)
    print("Successfully set SSID! Moving on...")
except:
    print("Task failed at process: WIFI_SSID_ENTRY")
    worksheet.update_cell(assetCell.row, (STATUS_INDEX + 1), "WIFI_SSID_ENTRY")
    driver.quit()
    exit()

##The name is ALWAYS available, however the password sometimes is not available, so we must
##use a try and except to avoid error
try:
    if(driver.find_element_by_xpath("//input[@type='password']").is_displayed()):
        passBox = driver.find_element_by_xpath("//input[@type='password']")
        passBox.clear()
        passBox.send_keys(wifiPassword)
        print("Successfully set password! Moving on...")
    else:
        ##Password box is not found
        driver.implicitly_wait(IMPLICIT_WAIT)
        typeMenu = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div[2]/div[2]/div/form/div[3]/div/div/div/input")
        typeMenu.click()

        driver.implicitly_wait(IMPLICIT_WAIT)

        passwordType = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/ul/li[2]")
        passwordType.click()

        driver.implicitly_wait(IMPLICIT_WAIT)

        passBox = driver.find_element_by_xpath("//input[@type='password']")
        passBox.clear()
        passBox.send_keys(wifiPassword)
        passBox.send_keys(Keys.CONTROL + "a")
        passBox.send_keys(Keys.DELETE)
        passBox.send_keys(wifiPassword)

except:
    try:
        print("Password box not found, attempting to resolve...")
        ##Password box is not found
        time.sleep(1)
        driver.implicitly_wait(IMPLICIT_WAIT)
        typeMenu = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div[2]/div[2]/div/form/div[3]/div/div/div/input")
        typeMenu.click()

        try:
            driver.implicitly_wait(IMPLICIT_WAIT)
            passwordType = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/ul/li[2]")
            passwordType.click()
        except:
            try:
                driver.implicitly_wait(IMPLICIT_WAIT)
                passwordType = driver.find_element_by_xpath("//div[6]/div/div/ul/li[2]")
                passwordType.click()
            except:
                driver.implicitly_wait(IMPLICIT_WAIT)
                passwordType = driver.find_element_by_xpath("//span[contains(.,'WPA2-PSK')]")
                passwordType.click()

        driver.implicitly_wait(IMPLICIT_WAIT)

        passBox = driver.find_element_by_xpath("//input[@type='password']")
        passBox.clear()
        passBox.send_keys(wifiPassword)
        passBox.send_keys(Keys.CONTROL + "a")
        passBox.send_keys(Keys.DELETE)
        passBox.send_keys(wifiPassword)

        print("Successfully set password! Moving on...")

    except:
        print("Task failed at process: WIFI_PASSWORD_ENTRY")
        worksheet.update_cell(assetCell.row, (STATUS_INDEX + 1), "WIFI_PASSWORD_ENTRY")
        driver.quit()
        exit()

##Apply changes made to the name and password

time.sleep(OTHER_WAIT)
try:
    driver.implicitly_wait(IMPLICIT_WAIT)
    applyBox = driver.find_element_by_xpath("/html/body/div/section/section/main/div[2]/div[2]/div/form/div[6]/div/button[1]/span")
    applyBox.click()
    print("Successfully saved changes! Moving on...")
except:
    try:
        driver.implicitly_wait(IMPLICIT_WAIT)
        newApplyBox = driver.find_element_by_css_selector(".el-form-item:nth-child(6) .el-button--primary > span")
        newApplyBox.click()
    except:
        try:
            driver.implicitly_wait(IMPLICIT_WAIT)
            newNewApplyBox = driver.find_element_by_xpath("//div[6]/div/button/span")
            newNewApplyBox.click()
        except:
            try:
                driver.implicitly_wait(IMPLICIT_WAIT)
                newNewNewApplyBox = driver.find_element_by_xpath("/html/body/div/section/section/main/div[2]/div[2]/div/form/div[5]/div/button[1]/span")
                newNewNewApplyBox.click()
            except:
                try:
                    driver.implicitly_wait(IMPLICIT_WAIT)
                    long = driver.find_element_by_css_selector("#app > section > section > main > div:nth-child(2) > div.el-card__body > div > form > div:nth-child(5) > div > button.el-button.el-button--primary.el-button--mini")
                    long.click()
                except:
                    print("Task failed at process: WIFI_SAVE_CHANGES")
                    worksheet.update_cell(assetCell.row, (STATUS_INDEX + 1), "WIFI_SAVE_CHANGES")
                    time.sleep(30)
                    driver.quit()
                    exit()

##Confirm changes
#<button type="button" class="el-button el-button--default el-button--small el-button--primary ">
#<!----><!---->
#<span>
#          Yes
#        </span></button>

time.sleep(OTHER_WAIT)
try:
    driver.implicitly_wait(IMPLICIT_WAIT)
    confirmBox = driver.find_element_by_xpath("//button[@type='button'][14]")
    confirmBox.click()
    print("Successfully confirmed changes! Moving on...")
except:
    try:
        driver.implicitly_wait(IMPLICIT_WAIT)
        otherBox = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/button[2]")
        otherBox.click()
        print("Successfully confirmed changes! Moving on...")
    except:
        try:
            #I hate that I have to do this but I do :(
            driver.implicitly_wait(IMPLICIT_WAIT)
            vague = driver.find_element_by_css_selector(".el-button--default:nth-child(2) > span")
            vague.click()
        except:
            try:
                trivialXpath = driver.find_element_by_xpath("//span[contains(.,'Yes')]")
                trivialXpath.click()
            except:
                try:
                    action = driver.find_element_by_tag_name("body")

                    action.send_keys(Keys.TAB)
                    action.send_keys(Keys.TAB)
                    action.send_keys(Keys.TAB)
                    action.send_keys(Keys.ENTER)
                except:
                    print("Task failed at process: WIFI_CONFIRM_CHANGES")
                    worksheet.update_cell(assetCell.row, (STATUS_INDEX + 1), "WIFI_CONFIRM_CHANGES")
                    driver.quit()
                    exit()

## Now we will navigate to the firewall settings
## Due to the nature of the localhost, we must load it, then unload it
## then load it again (and give it ample time for each)

time.sleep(OTHER_WAIT)

driver.get("http://192.168.0.1/#/FireWall")
time.sleep(OTHER_WAIT)

driver.get("http://192.168.0.1/#/DeviceSettings")
time.sleep(WEBPAGE_LOAD_TIME)

if(unlikelyPassword and FIX_PASSWORD):
    try:
        driver.implicitly_wait(IMPLICIT_WAIT)
        currentPassword = driver.find_element_by_xpath("//input")
        currentPassword.click()
        currentPassword.send_keys(UNLIKELY_PASSWORD)
    except:
        print("Task failed at process: UNLIKELY_PASSWORD_ENTRY")
        driver.quit()
        exit()

    try:
        driver.implicitly_wait(IMPLICIT_WAIT)
        newPassword = driver.find_element_by_xpath("//div[2]/div/div/input")
        newPassword.click()
        newPassword.send_keys(LIKELY_PASSWORD)
    except:
        print("Task failed at process: LIKELY_PASSWORD_ENTRY_INITIAL")
        driver.quit()
        exit()

    try:
        driver.implicitly_wait(IMPLICIT_WAIT)
        newPasswordConfirm = driver.find_element_by_xpath("//div[3]/div/div/input")
        newPasswordConfirm.click()
        newPasswordConfirm.send_keys(LIKELY_PASSWORD)
    except:
        print("Task failed at process: LIKELY_PASSWORD_ENTRY_CONFIRM")
        driver.quit()
        exit()

    try:
        driver.implicitly_wait(IMPLICIT_WAIT)
        confirmNewPassword = driver.find_element_by_xpath("//span[contains(.,'Apply')]")
        confirmNewPassword.click()
    except:
        print("Task failed at process: PASSWORD_CHANGE_CONFIRM")
        driver.quit()
        exit()


driver.get("http://192.168.0.1/#/NetworkSettings")
time.sleep(WEBPAGE_LOAD_TIME)

try:
    driver.implicitly_wait(IMPLICIT_WAIT)
    apnSelector = driver.find_element_by_css_selector(".el-form:nth-child(2) > .el-form-item:nth-child(2) .el-input__inner")
    apnSelector.click()
    print("Successfully selected the APN dropdown! Moving on...")
except:
    print("Task failed at process: APN_DROPDOWN_SELECT")
    worksheet.update_cell(assetCell.row, (STATUS_INDEX + 1), "APN_DROPDOWN_SELECT")
    driver.quit()
    exit()

try:
    driver.implicitly_wait(IMPLICIT_WAIT)
    TMobile = driver.find_element_by_css_selector(".hover")
    TMobile.click()
    print("Successfully selected T-MOBILE from dropdown! Moving on...")
except:
    try:
        driver.implicitly_wait(1.5)
        TMobileAgain = driver.find_element_by_xpath("//li[contains(.,'T-Mobile US')]")
        TMobileAgain.click()
        print("Successfully selected T-MOBILE from dropdown! Moving on...")
    except:
        print("Task failed at process: APN_PROFILE_SELECT")
        worksheet.update_cell(assetCell.row, (STATUS_INDEX + 1), "APN_PROFILE_SELECT")
        driver.quit()
        exit()

try:
    driver.implicitly_wait(IMPLICIT_WAIT)
    setButton = driver.find_element_by_css_selector("css=.el-form-item:nth-child(9) .el-button--primary > span")
    setButton.click()
except:
    try:
        driver.implicitly_wait(IMPLICIT_WAIT)
        otherSetButton = driver.find_element_by_xpath("//div[@id='app']/section/section/main/div/div[4]/div/div[3]/div[2]/div/form/div[9]/div/button/span")
        otherSetButton.click()
    except:
        print("APN Confirm was not selected (not an error)")

driver.get("http://192.168.0.1/#/Firewall")
time.sleep(WEBPAGE_LOAD_TIME)

## Reset to disabled
try:
    if((driver.find_element_by_xpath("//div[2]/div/div/input").is_displayed()) == False):
        driver.implicitly_wait(2)
        dropdownMAC = driver.find_element_by_xpath("//input[@type='text']")
        dropdownMAC.click()
        print("Successfully selected MAC dropdown! Moving on...")
        driver.implicitly_wait(2)
        whitelist = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/ul/li[2]")
        whitelist.click()
        print("Successfully selected whitelist from MAC dropdown! Moving on...")
except:
    print("Task failed at process: MAC_DROPDOWN_SELECT")
    worksheet.update_cell(assetCell.row, (STATUS_INDEX + 1), "MAC_DROPDOWN_SELECT")
    driver.quit()
    exit()

time.sleep(OTHER_WAIT)

try:
    driver.implicitly_wait(1)
    nicknameStudent = driver.find_element_by_xpath("//div[2]/div/div/input")
    nicknameStudent.clear()
    nicknameStudent.send_keys(assetNumber)
    print("Successfully added student MAC (asset)! Moving on...")
    time.sleep(0.5)
except:
    print("Task failed at process: MAC_ADD_STUDENTID")
    worksheet.update_cell(assetCell.row, (STATUS_INDEX + 1), "MAC_ADD_STUDENTID")
    driver.quit()
    exit()

try:
    driver.implicitly_wait(1)
    addressStudent = driver.find_element_by_css_selector(".el-form-item:nth-child(3) .el-input__inner")
    addressStudent.clear()
    addressStudent.send_keys(macAddress)
    print("Successfully added student MAC (address)! Moving on...")
    time.sleep(0.5)
except:
    print("Task failed at process: MAC_ADD_STUDENTADDY")
    worksheet.update_cell(assetCell.row, (STATUS_INDEX + 1), "MAC_ADD_STUDENTADDY")
    driver.quit()
    exit()

try:
    driver.implicitly_wait(1)
    submitStudent = driver.find_element_by_xpath("//div[4]/div/button")
    submitStudent.click()
    print("Successfully saved student MAC credentials! Moving on...")
    time.sleep(0.5)
except:
    print("Task failed at process: MAC_ADD_STUDENT")
    worksheet.update_cell(assetCell.row, (STATUS_INDEX + 1), "MAC_ADD_STUDENT")
    driver.quit()
    exit()

time.sleep(OTHER_WAIT)

try:
    if(driver.find_element_by_xpath("//span[contains(.,'OK')]").is_displayed()):
        # Click
        driver.find_element_by_xpath("//span[contains(.,'OK')]").click()
except:
  print("MAC Address was added successfully (not a duplicate)")

## Add first admin mac address
#try:
#    driver.implicitly_wait(1)
#    nicknameAdminOne = driver.find_element_by_xpath("//div[2]/div/div/input")
#    nicknameAdminOne.click()
#    nicknameAdminOne.send_keys("A000031388")
#    nicknameAdminOne.send_keys(Keys.CONTROL + "a");
#    nicknameAdminOne.send_keys(Keys.DELETE)
#    time.sleep(0.5)
#    nicknameAdminOne.send_keys("A000031388")
#    print("Successfully added first admin MAC (asset)! Moving on...")
#except:
#    print("Task failed at process: MAC_ADMIN_ADDID_ONE")
#    worksheet.update_cell(assetCell.row, (STATUS_INDEX + 1), "MAC_ADMIN_ADDID_ONE")
#    driver.quit()
#    exit()
#
#try:
#    driver.implicitly_wait(1)
#    addressAdminOne= driver.find_element_by_xpath("//div[3]/div/div/input")
#    addressAdminOne.click()
#    addressAdminOne.send_keys(Keys.CONTROL + "a");
#    addressAdminOne.send_keys("d4:d2:52:55:2f:a8")
#    addressAdminOne.send_keys(Keys.CONTROL + "a");
#    addressAdminOne.send_keys(Keys.DELETE)
#    addressAdminOne.send_keys("d4:d2:52:55:2f:a8")
#    print("Successfully added first admin MAC (address)! Moving on...")
#    time.sleep(0.5)
#except:
#    print("Task failed at process: MAC_ADMIN_ADDMAC_ONE")
#    worksheet.update_cell(assetCell.row, (STATUS_INDEX + 1), "MAC_ADMIN_ADDMAC_ONE")
#    driver.quit()
#    exit()
#
#try:
#    driver.implicitly_wait(1)
#    submitAdminOne = driver.find_element_by_xpath("//div[4]/div/button")
#    submitAdminOne.click()
#    print("Successfully added first admin MAC credentials! Moving on...")
#    time.sleep(0.5)
#except:
#    print("Task failed at process: MAC_ADMIN_ADD_ONE")
#    worksheet.update_cell(assetCell.row, (STATUS_INDEX + 1), "MAC_ADMIN_ADD_ONE")
#    driver.quit()
#    exit()
#
#time.sleep(OTHER_WAIT)

# Check if rule already exists
#try:
#    driver.implicitly_wait(IMPLICIT_WAIT)
#    if(driver.find_element_by_xpath("//span[contains(.,'OK')]").is_displayed()):
#        # Click
#        driver.find_element_by_xpath("//span[contains(.,'OK')]").click()
#except:
#  print("MAC Address was added successfully (not a duplicate)")

## Add second admin mac address
#try:
#    driver.implicitly_wait(2)
#    nicknameAdminTwo = driver.find_element_by_xpath("//div[2]/div/div/input")
#    nicknameAdminTwo.click()
#    nicknameAdminTwo.send_keys("A000060098")
#    nicknameAdminTwo.send_keys(Keys.CONTROL + "a");
#    nicknameAdminTwo.send_keys(Keys.DELETE)
#    nicknameAdminTwo.send_keys("A000060098")
#    print("Successfully added second MAC (asset)! Moving on...")
#    time.sleep(0.5)
#except:
#    print("Task failed at process: MAC_ADD_ADMINID_TWO")
#    worksheet.update_cell(assetCell.row, (STATUS_INDEX + 1), "MAC_ADD_ADMINID_TWO")
#    driver.quit()
#    exit()
#
#
#try:
#    driver.implicitly_wait(1)
#    addressAdminTwo = driver.find_element_by_xpath("//div[3]/div/div/input")
#    addressAdminTwo.click()
#    addressAdminTwo.send_keys(Keys.CONTROL + "a");
#    addressAdminTwo.send_keys("48:89:e7:03:34:b9")
#    addressAdminTwo.send_keys(Keys.CONTROL + "a");
#    addressAdminTwo.send_keys(Keys.DELETE)
#    addressAdminTwo.send_keys("48:89:e7:03:34:b9")
#    print("Successfully added second MAC (address)! Moving on...")
#    time.sleep(0.5)
#except:
#    print("Task failed at process: MAC_ADD_ADMINMAC_TWO")
#    worksheet.update_cell(assetCell.row, (STATUS_INDEX + 1), "MAC_ADD_ADMINMAC_TWO")
#    exit()
#
#try:
#    driver.implicitly_wait(1)
#    submitAdminTwo = driver.find_element_by_xpath("//div[4]/div/button")
#    submitAdminTwo.click()
#    print("Successfully added second MAC credentials! Moving on...")
#    time.sleep(0.5)
#except:
#    print("Task failed at process: MAC_ADD_ADMIN_TWO")
#    worksheet.update_cell(assetCell.row, (STATUS_INDEX + 1), "MAC_ADD_ADMIN_TWO")
#    driver.quit()
#    exit()

#time.sleep(OTHER_WAIT)

# Check if rule already exists
#try:
#    driver.implicitly_wait(IMPLICIT_WAIT)
#    if(driver.find_element_by_xpath("//span[contains(.,'OK')]").is_displayed()):
#        # Click
#        driver.find_element_by_xpath("//span[contains(.,'OK')]").click()
#except:
#  print("MAC Address was added successfully (not a duplicate)")

if(WORKSHEET_PUSH):
    ##Reference: [CB_ASSET, CB_MAC, HS_ASSET, HS_SSID, HS_PASS, STATUS]
    outputSheet = macAddresses.worksheet(WORKSHEET_PUSH_NAME)

    outputSheet.append_row([assetNumber, macAddress, hotspotAsset, wifiName, wifiPassword, 'Success!'])

if(REGISTER):
    ##Reference: Student_ID, CB_ASSET, CB_SERIAL, HS_ASSET
    registrySheet.append_row([studentID, assetNumber, serialNumber, hotspotAsset])

print(" ")
print("Success! The script has completed! To run another, simply type: ")
print("|> python main.py  OR  UP-ARROW")
print(" ")
driver.quit()

worksheet.update_cell(assetCell.row, (STATUS_INDEX + 1), "Success!")

exit()