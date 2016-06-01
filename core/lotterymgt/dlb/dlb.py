from __init__ import *


def getDataFromDLB():
    dlb_result_list = {}
    data = requests.get(LotteryMgtDLB.dlb_data_fetch).content
    DLB_lottery_list = BeautifulSoup(data).find_all("option")
    for i in DLB_lottery_list:
        dlb_result_list[i.text] = i.get('value', '')
    return dlb_result_list


def getDLBResult(dn, index, DataList):
    wining_numbers_set = ""
    if index <= len(DataList):
        result = urllib2.Request(LotteryMgtDLB.dlb_data_result,
                                 urlencode({"db": DataList.values()[index], "dn": dn, "ename": ""}).encode())
        for i in BeautifulSoup(urllib2.urlopen(result).read().decode()).findAll("div", {"align": "right"}):
            wining_numbers_set += i.string
        if wining_numbers_set == "":
            return "Wrong dn"
        else:
            return wining_numbers_set
    else:
        return "Wrong Index"

# print getDLBResult("1266", 0)
