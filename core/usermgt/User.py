class User:
    def __init__(self,
                 address = "",
                 index = 0,
                 messageFlow = 0,
                 lotteryList=[],
                 count=0):
        """
        :param address: User Phone Number
        :param index: session index
        :param messageFlow: user message flow number
        :param lotteryList: user previous lottery details
        :param count: user app used count
        """
        self.count = count
        self.lotteryList = lotteryList
        self.messageFlow = messageFlow
        self.index = index
        self.address = address