from core.lotterymgt.dlb.dlb import *


dataList = getDataFromDLB()
print len(dataList)
print dataList
result = getDLBResult("4", 7, dataList)
result = result.decode("utf8")
result = result.replace('\xc2\xa0', ' ')
print result