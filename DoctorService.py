import FileUtil

class DoctorService:
    NAME_FILE_WITH_PAINS_LIST = "Pains.txt"
    NAME_FILE_WITH_ALL_USERS = "Users.txt"

    def addPain(self, painId):
        FileUtil.FileUtil().writeToFile(str(painId), self.NAME_FILE_WITH_PAINS_LIST)

    def getAllPainsList(self):
        FileUtil.FileUtil().sortFileContents(self.NAME_FILE_WITH_PAINS_LIST)
        return FileUtil.FileUtil().getAllFromFile(self.NAME_FILE_WITH_PAINS_LIST)
    
    def getOnePain(self, painId):
        return FileUtil.FileUtil().getFromFile(str(painId), self.NAME_FILE_WITH_PAINS_LIST)

    def deleteOnePain(self, painId):
        FileUtil.FileUtil().deleteSpecifiedLine(self.NAME_FILE_WITH_PAINS_LIST, str(painId))

           