import datetime
import FileUtil
import UserView

class BureacracyService:
    def makeViscera(self, email):
        now = datetime.datetime.now()
        formatted_date = now.strftime("%Y-%m-%d")
        formatted_time = now.strftime("%H:%M")
        fileName = email+".txt"
        value = str(formatted_date)+ " " + str(formatted_time) + " " +email
        FileUtil.FileUtil().writeToFile(value, fileName)

    def viewViscera(self, email):
        listViscera = FileUtil.FileUtil().getAllFromFile(email+".txt")
        