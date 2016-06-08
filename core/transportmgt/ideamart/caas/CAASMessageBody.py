class CAASmessageBody:
    def __init__(self, password="",
                 url="",
                 SubscriberId="",
                 applicationID="",
                 ExternalTrxId="",
                 Amount=""):
        self.Amount = Amount
        self.ExternalTrxId = ExternalTrxId
        self.SubscriberId = SubscriberId
        self.applicationID = applicationID
        self.url = url
        self.password = password