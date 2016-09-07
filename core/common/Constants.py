from core.dbmgt.getConnection import *


class LotteryMgtDLB:
    def __init__(self):
        pass

    dlb_data_fetch = "http://dlb.today/dlb/"
    dlb_data_result = "http://www.dlb.today/dlb/index.php?option=com_jumi&fileid=31&Itemid=31"


class LotteryMgtNLB:
    def __init__(self):
        pass

    nlb_data_fetch = "http://www.nlb.lk/lotteries.php"
    nlb_data_result = "http://www.nlb.lk/"
    nlb_show_result = "show-results.php?lott="


class Ideamart:
    def __init__(self):
        pass

    Amount = "5"
    # Run in Host
    appId = "APP_024442"
    password = "0dcd163c817972cdf74a81446f8f8b3f"
    SMSUrl = "https://api.dialog.lk/sms/send"
    USSDUrl = "https://api.dialog.lk/ussd/send"
    CAASUrl = "https://api.dialog.lk/caas/direct/debit"
    SubscriptionUrl = "https://api.dialog.lk/subscription/send"
    # Run locally
    # appId = "APP_000001"
    # password = "password"
    # SMSUrl = "http://localhost:7000/sms/send"
    # USSDUrl = "http://localhost:7000/ussd/send"
    # CAASUrl = "http://localhost:7000/caas/direct/debit"
    # SubscriptionUrl = "http://localhost:7000/subscription/send"


class Application:
    def __init__(self):
        pass

    index = 0
    messageFlow = 0
    nlbListSize = 0
    dlbListSize = 0
    nlbList = {}
    dlbList = {}
    ErrorMessage = "Please Enter a number between given choices" + "\n" + "0. Back" + "\n" + "000. Exit"
    getDrawNumber = "Please Enter draw number(Dinum wara ankaya)" + "\n" + "0. Back" + "\n" + "000. Exit"
    EndMessage = "Thank You For use." + "\n" + "lottery anka balanna #775*910# number eka save kara ganna"
    initSMS = "Lottery Result balanna #775*910# ankaya save kara ganna"
    regMessage = "1. Register"

class DatabaseCollections:
    def __init__(self):
        pass

    userCollection = getDatabase().userCollection
