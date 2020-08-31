import gspread

ROOT_DIRECTORY = r"C:\Users\gfoy\Documents\Complete\src"
REGISTER_NAME = "Garrett"
REGISTER_KEY = '18VHRgCU2FIwYCkXBmLXc2QKSbCOXff0mw6DMpC1b8tA'
SERVICE_BOT = r"\service_bot.json"

gc = gspread.service_account(filename=ROOT_DIRECTORY + SERVICE_BOT)
registry = gc.open_by_key(REGISTER_KEY)
registrySheet = registry.worksheet(REGISTER_NAME)

while(True):

    CB_ASSET = input("Please scan the CHROMEBOOK ASSET TAG: ")
    CB_SERIAL = input("Please scan the CHROMEBOOK SERIAL NUMBER: ")
    HS_ASSET = input("Please scan the HOTSPOT ASSET TAG:")
    STUDENT_ID = input("Please scan the STUDENT ID: ")

    ##Reference: Student_ID, CB_ASSET, CB_SERIAL, HS_ASSET
    registrySheet.append_row([STUDENT_ID, CB_ASSET, CB_SERIAL, HS_ASSET])

    for x in range(15):
        print(" ")
    print("Credentials added! For reference the chromebook asset number was: " + CB_ASSET)
    for x in range(5):
        print(" ")