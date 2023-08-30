class BureaucracyModel:
    def __init__(self):
        self.arr1 = []  # Define arr1 as an instance variable

    def listAllBureaucracy(self, arr):
        self.arr1 = arr  # Assign arr to the instance variable arr1
        return self.arr1

    def getOneBureaucracy(self, index):
        if 0 <= index < len(self.arr1):  # Check if the index is within bounds
            return self.arr1[index]
        else:
            return None  # Return None if the index is out of bounds

    def writeAssignment(self, pain_id, drug_id):
        f = open("Assignment.txt", "w")
        f.write(drug_id + ' ' + pain_id + "\n")
        f.close()

    def checkAssignment(self, pain_id, drug_id):
        f = open("Assignment.txt", "r")
        lines = f.readlines()
        for line in lines:
            index1 = line.find(" ")
            index2 = line.find("\n")
            temp_pain_id = line[:index1]
            temp_drug_id = line[index1+1:index2]
            if(temp_pain_id == pain_id and temp_drug_id == drug_id):
                f.close()
                raise Exception("Assignment already exist")
        f.close()
        return True