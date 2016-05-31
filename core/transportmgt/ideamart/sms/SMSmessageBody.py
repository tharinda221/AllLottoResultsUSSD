class SMSmessageBody:
    def __init__(self, message="",
                 password="",
                 url="",
                 destAddress="",
                 applicationID=""):
        self.applicationID = applicationID
        self.destAddress = destAddress
        self.url = url
        self.password = password
        self.message = message

