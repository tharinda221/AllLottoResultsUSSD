from __init__ import *


def getDataFromDLB():
    list = []
    paramList = []
    data = requests.get(LotteryMgtDLB.dlb_data_fetch).content
    DLB_lottery_list = BeautifulSoup(data).find_all("option")
    for i in DLB_lottery_list:
        list.append(i.text)
        paramList.append(i.get('value', ''))
        # print i.text, " ", i.get('value', '')
    return list, paramList


def getDLBResult(dn, index):
    DataList, paramList = getDataFromDLB()
    wining_numbers = []
    if index <= len(DataList):
        result = urllib2.Request(LotteryMgtDLB.dlb_data_result,
                                 urlencode({"db": paramList[index], "dn": dn, "ename": ""}).encode())
        for i in BeautifulSoup(urllib2.urlopen(result).read().decode()).findAll("div", {"align": "right"}):
            wining_numbers.append(i.string)
        if len(wining_numbers) == 0:
            return "Wrong dn"
        else:
            return wining_numbers
    else:
        return "Wrong Index"


#print getDLBResult("1266", 2)
