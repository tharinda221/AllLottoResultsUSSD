from core.usermgt.User import User
from core.usermgt.UserDAO import UserDAO

def test():
    #user = User(address="0711834769", index=0, messageFlow=0, lotteryList=[{"Shanida":0}, {"lottery":5}], count=0)
    dao = UserDAO()
    user = dao.getUser("0711834769")
    print user.address


test()