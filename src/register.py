import gspread
import config

def register(CB_ASSET, CB_SERIAL, HS_ASSET, STUDENT_ID):

    ROOT_DIRECTORY = (config.getRootDirectory())
    REGISTER_NAME = config.getSheetName()
    REGISTER_KEY = config.getRegisterKey()
    SERVICE_BOT = r"\service_bot.json"

    gc = gspread.service_account(filename=ROOT_DIRECTORY + SERVICE_BOT)
    registry = gc.open_by_key(REGISTER_KEY)
    registrySheet = registry.worksheet(REGISTER_NAME)
    registrySheet.append_row([STUDENT_ID, CB_ASSET, CB_SERIAL, HS_ASSET])