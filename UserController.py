import smtplib, ssl
import UserModel
import hashlib
import UserView

class UserController:
    def __init__(self):
        self.receiver_email = "dmytro2607@gmail.com"
        self.message = """\
        Subject: Hi there123
        
        This message is sent from Python."""

    def register(self, password, sender_email):
        smtp_server = "smtp.elasticemail.com"
        port = 2525  # For starttls
        try:
            UserModel.UsersModel().checkUser(sender_email)
        except Exception as e:
            print(e)
            # return False
        # Create a secure SSL context
        # context = ssl.create_default_context()

        # Try to log in to server and send email
        try:
            # server = smtplib.SMTP(smtp_server, port)
            # server.ehlo()  # Can be omitted
            # server.starttls(context=context)  # Secure the connection
            # server.ehlo()  # Can be omitted
            # server.login(sender_email, password)
            # response = server.sendmail(sender_email, self.receiver_email, self.message)
            # print(response)
            # qwa = UserModel.UsersModel()
            # qwa.addUser(# print(password1)
            # print(hashlib.md5(password.encode()).hexdigest())sender_email, password)
            UserModel.UsersModel().addUser(sender_email, password)
        except Exception as e:
            # Print any error messages to stdout
            print(e)
        finally:
            pass
            # server.quit()

    # put login in database
    def login(self, password, sender_email):
        try:
            line = UserModel.UsersModel().getUser(sender_email)
            password1 = line[:32]
            print(password1)
            print(hashlib.md5(password.encode()).hexdigest())
            if hashlib.md5(password.encode()).hexdigest() != password1:
                raise Exception("Wrong Password")
        except Exception as e:
            print(e)
        finally:
            return True

    def ViewAllUsers(self):
        listUsers = UserModel.UsersModel().listAllUsers()
        print(listUsers)
        UserView.UserView().MakeHtml(listUsers)

x = UserController()
# x.register("123", "123@gmail.com")
# print(x.login("4E5067C7A00E6F51EA53EA6CCEAF926AFD6C", "dmytro26070707@gmail.com"))
x.ViewAllUsers()