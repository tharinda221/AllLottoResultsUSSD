from core.lotterymgt.dlb.dlb import *

dataList = getDataFromDLB()
print len(dataList)
print dataList
print getDLBResult("1985", 7, dataList)