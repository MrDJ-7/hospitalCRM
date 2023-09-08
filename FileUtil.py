import HelperUtil


class FileUtil:
    def sortFileContents(self, fileName):
        with open(fileName, "r") as file:
            lines = file.readlines()
        file.close()

        lines = HelperUtil.HelperUtil().bubblesort(lines)

        with open(fileName, "w") as file:
            file.writelines(lines)
        file.close()

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

    def getAllFromFile(self, fileName):
        listFile = []
        # print(str(fileName))
        f = open(fileName, "r")
        lines = f.readlines()
        for line in lines:
            index = line.find("\n")
            listFile.append(line[:index])
        f.close()
        return listFile

    def deleteSpecifiedLine(self, fileName, string_to_remove):
        # Считайте содержимое файла
        with open(fileName, "r") as file:
            lines = file.readlines()
        file.close()

        # Удалите строку из списка lines, если она существует
        new_lines = [line for line in lines if line.strip() != string_to_remove]

        # Запишите обновленное содержимое обратно в файл
        with open(fileName, "w") as file:
            file.writelines(new_lines)
        file.close()
