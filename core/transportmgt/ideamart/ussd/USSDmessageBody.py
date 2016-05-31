class USSDmessageBody:
    def __init__(self, message="",
                 password="",
                 url="",
                 destAddress="",
                 applicationID="",
                 encording="",
                 sessionId="",
                 ussdOperation="",
                 version=""):
        self.version = version
        self.ussdOperation = ussdOperation
        self.sessionId = sessionId
        self.encording = encording
        self.applicationID = applicationID
        self.destAddress = destAddress
        self.url = url
        self.password = password
        self.message = message

