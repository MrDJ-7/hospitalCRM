import hashlib
import FileUtil


class UsersModel:
    def __init__(self):
        self.arr1 = []  # Define arr1 as an instance variable

    def listAllUsers(self):
        listEmail = FileUtil.FileUtil.getAllFromFile("Users.txt")
        for i in range(len(listEmail)):
            listEmail[i] = listEmail[i][33:]
        return listEmail

    def getOneUser(self, index):
        if 0 <= index < len(self.arr1):  # Check if the index is within bounds
            return self.arr1[index]
        else:
            return None  # Return None if the index is out of bounds

    def addUser(self, email, password):
        x = hashlib.md5(password.encode()).hexdigest() + ' ' + email
        FileUtil.FileUtil().writeToFile(x, "Users.txt")


    def getUser(self, email):
        try:
            x = FileUtil.FileUtil().getFromFile(email, "Users.txt")
        except Exception as e:
            print(e)
        finally:
            return x

    def checkUser(self, email):
        try:
            x = FileUtil.FileUtil().getFromFile(email, "Users.txt")
        except Exception as e:
            raise Exception("this email already exists")
        finally:
            return True
# qwa = UsersModel()
#
# # Define a list of drug dictionaries
# a1 = {'id': '24', 'name': 'Dima', 'last_name': 'Ryan', 'status_id': '0'}
# a2 = {'id': '2', 'name': 'Artur', 'last_name': 'Morgan', 'status_id': '1'}
# a3 = {'id': '4', 'name': 'Buker', 'last_name': 'De', 'status_id': '3'}
#
# a = [a1, a2, a3]
#
#
# # Use the getOneDrug method to retrieve a drug by index
# print(qwa.listAllUsers(a))
# print(qwa.getOneUser(1))  # Output: {'id': '32', 'name': 'nixar'}
# qwa.addUser("asdsdas", "alll")