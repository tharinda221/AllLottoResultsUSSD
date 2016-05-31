from __init__ import *


def getDataFromNLB():
    nlb_result_list = {}
    data = requests.get(LotteryMgtNLB.nlb_data_fetch).content
    NLB_lottery_list = BeautifulSoup(data).find_all("a", {"class": "bodyText"})
    for i in NLB_lottery_list:
        changed_url = str(
            LotteryMgtNLB.nlb_data_result + str(i.get("href")).replace("lot", "id").replace("info", "more"))
        nlb_result_list[i.text] = changed_url.replace("http://www.nlb.lk/results-more.php?id=", "")
    return nlb_result_list


def getNLBResult(dn, index, dataList):
    lista = []
    if index <= len(dataList):
        lot = dataList.values()[index]
        data = requests.get(LotteryMgtNLB.nlb_data_result + LotteryMgtNLB.nlb_show_result + lot + "&dno=" + dn).content
        soup = BeautifulSoup(data)
        try:
            wining_numbers = soup.find("table", {"class": "lottery-numbers"}).find_all("td")
            for a in wining_numbers:
                lista.append(str(a.text).replace(" ", ""))
            return str(lista).replace("n", "").replace("'", "").replace("[", "").replace("]", "").replace(",",
                                                                                                          "").replace(
                "t",
                "").replace(
                "\\", "")
        except:
            return "wrong dn"
    else:
        return "wrong index"


# print getDataFromNLB().values()
#print getNLBResult("4", 0)
