from __init__ import *

import sys

reload(sys)
sys.setdefaultencoding('utf8')

def getDataFromDLB():
    dlb_result_list = {}
    data = requests.get(LotteryMgtDLB.dlb_data_fetch).content
    DLB_lottery_list = BeautifulSoup(data, "html5lib").find_all("option")
    for i in DLB_lottery_list:
        dlb_result_list[i.text] = i.get('value', '')
    return dlb_result_list


def getDLBResult(dn, index, DataList):
    wining_numbers_set = ""
    if index <= len(DataList):
        result = urllib2.Request(LotteryMgtDLB.dlb_data_result,
                                 urlencode({"db": DataList.values()[index], "dn": dn, "ename": ""}).encode())
        numberList = BeautifulSoup(urllib2.urlopen(result).read().decode(), "html5lib").findAll("div", {"align": "right"})
        numberList.pop(0)
        for i in numberList:
            wining_numbers_set += i.string
        if wining_numbers_set == "":
            return "Oba yomu kala dinum wara ankaya waradiya nathohoth thama dinum ada nomatha"
        else:
            return wining_numbers_set
    else:
        return "Wrong Index"

# print getDLBResult("1266", 0)
