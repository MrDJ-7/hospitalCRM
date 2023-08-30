import hashlib


class UsersModel:
    def __init__(self):
        self.arr1 = []  # Define arr1 as an instance variable

    def listAllUsers(self, arr):
        self.arr1 = arr  # Assign arr to the instance variable arr1
        return self.arr1

    def getOneUser(self, index):
        if 0 <= index < len(self.arr1):  # Check if the index is within bounds
            return self.arr1[index]
        else:
            return None  # Return None if the index is out of bounds

    def addUser(self, email, password):
        f = open("Users.txt", "w")
        result = hashlib.md5(password.encode())
        f.write(result.hexdigest() + ' ' + email + " \n")
        f.close()

    def getUser(self, email):
        f = open("Users.txt", "r")
        # string to search in file
        lines = f.readlines()
        for line in lines:
            # check if string present on a current line
            if line.find(email) != -1:
                f.close()
                return line
        f.close()
        raise Exception("User Not Found")

    def checkUser(self, email):
        f = open("Users.txt", "r")
        # string to search in file
        lines = f.readlines()
        for line in lines:
            # check if string present on a current line
            if line.find(email) != -1:
                f.close()
                raise Exception("this email already exists")
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