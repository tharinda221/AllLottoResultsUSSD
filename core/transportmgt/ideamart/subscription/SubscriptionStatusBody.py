class SubscriptionMessageBody:
    def __init__(self, subscriberId="",
                 password="",
                 url="",
                 applicationID=""
                 ):
        self.subscriberId = subscriberId
        self.applicationID = applicationID
        self.url = url
        self.password = password