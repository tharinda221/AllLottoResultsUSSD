class SubscriptionMessageBody:
    def __init__(self, subscriberId="",
                 password="",
                 url="",
                 applicationID="",
                 action="",
                 version=""):
        self.version = version
        self.action = action
        self.subscriberId = subscriberId
        self.applicationID = applicationID
        self.url = url
        self.password = password