class FileUtil:
    def getFromFile(self, needle, haystack):
        f = open(haystack, "r")
        lines = f.readlines()
        for line in lines:
            if line.find(needle) != -1:
                f.close()
                return line
        f.close()
        raise Exception("String not found")

    def writeToFile(self, value, target):
        with open(target, "a") as f:
            f.write(value + "\n")
    def getAllFromFile(fileName):
        listFile = []
        f = open(fileName, "r")
        lines = f.readlines()
        for line in lines:
            index = line.find("\n")
            listFile.append(line[:index])
        f.close()
        return listFile
