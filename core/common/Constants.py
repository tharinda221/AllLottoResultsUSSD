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

    password = "0dcd163c817972cdf74a81446f8f8b3f"
    SMSUrl = "http://api.dialog.lk/sms/send"
    USSDUrl = "http://api.dialog.lk/ussd/send"


class Application:
    def __init__(self):
        pass

    index = 0
    messageFlow = 0
    nlbListSize = 0
    dlbListSize = 0
    nlbList = {}
    dlbList = {}
    ErrorMessage = "Please Enter a number between given choices" + "\n" + "0. Back" + "\n" + "99. Exit"
    getDrawNumber = "Please Enter draw number(Dinum wara ankaya)" + "\n" + "0. Back" + "\n" + "99. Exit"
