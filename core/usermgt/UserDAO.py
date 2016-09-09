from core.common.Constants import *
from core.usermgt.User import User


class UserDAO:
    def __init__(self):
        pass

    def createUser(self, user):
        """
        Create a new user and store in database
        :param user: User object
        """
        dao = UserDAO()
        if dao.userExist(user.address):
            DatabaseCollections.userCollection.insert_one(
                {
                    "address": user.address,
                    "index": user.index,
                    "messageFlow": user.messageFlow,
                    "lotteryList": user.lotteryList,
                    "count": user.count,
                    "newUser": user.newUser
                }
            )
        else:
            dao.updateUserElder(user.address, "False")
            count = dao.getUser(user.address).count
            dao.updateUserCount(user.address, count+1)
            dao.updateUserMessageFlow(user.address, 1)

    def userExist(self, address):
        if DatabaseCollections.userCollection.find({"address": address}).count() > 0:
            return False
        else:
            return True

    def updateUserIndex(self, address, index):
        """
        Update user index
        :param address: Phone number of the user that need to be updated.
        :param index: Id of a lottery request by user
        :return: True or False
        """
        try:
            DatabaseCollections.userCollection.update_one(
                {
                    "address": address
                },
                {"$set": {
                    "index": index
                }})
            return True
        except IOError:
            return False

    def updateUserElder(self, address, newUser):
        """
        Update user message flow
        :param address: Phone number of the user that need to be updated.
        :param messageFlow: user message flow number
        :return: True or False
        """
        try:
            DatabaseCollections.userCollection.update_one(
                {
                    "address": address
                },
                {"$set": {
                    "newUser": newUser
                }})
            return True
        except IOError:
            return False

    def updateUserMessageFlow(self, address, messageFlow):
        """
        Update user message flow
        :param address: Phone number of the user that need to be updated.
        :param messageFlow: user message flow number
        :return: True or False
        """
        try:
            DatabaseCollections.userCollection.update_one(
                {
                    "address": address
                },
                {"$set": {
                    "messageFlow": messageFlow
                }})
            return True
        except IOError:
            return False

    def updateUserCount(self, address, count):
        """
        Update user count
        :param address: Phone number of the user that need to be updated.
        :param count: App used Count of the user
        :return: True or False
        """
        try:
            DatabaseCollections.userCollection.update_one(
                {
                    "address": address
                },
                {"$set": {
                    "count": count
                }})
            return True
        except IOError:
            return False

    def updateUserLotteryList(self, address, lotteryList):
        """
        Update user count
        :param address: Phone number of the user that need to be updated.
        :param lotteryList: Lottery List that user used previously
        :return: True or False
        """
        try:
            DatabaseCollections.userCollection.update_one(
                {
                    "address": address
                },
                {"$set": {
                    "lotteryList": lotteryList
                }})
            return True
        except IOError:
            return False

    def getUser(self, address):
        """
        Return User
        :param address: Phone number of the user.
        :param address: App used Count of the user
        :return: List
        """
        data = DatabaseCollections.userCollection.find_one({"address": address})
        if data is None:
            return None
        else:
            user = User(data["address"], data["index"], data["messageFlow"], data["lotteryList"], data["count"], data["newUser"])
            return user