import BureaucracyModel

class DoctorController():
    def __init__(self):
        self.arr1 = []  # Define arr1 as an instance variable

    def listAllPains(self, arr):
        self.arr1 = arr  # Assign arr to the instance variable arr1
        return self.arr1

    def getOnePain(self, index):
        if 0 <= index < len(self.arr1):  # Check if the index is within bounds
            return self.arr1[index]
        else:
            return None  # Return None if the index is out of bounds

    def AssignmentDrugs(self, pain_id, drug_id):
        try:
            BureaucracyModel.BureaucracyModel().checkAssignment(pain_id, drug_id)
            BureaucracyModel.BureaucracyModel().writeAssignment(pain_id, drug_id)
        except Exception as e:
            print(e)


# qwa = DoctorControler()
# qwa.AssignmentDrugs("1", "1")
# qwa.AssignmentDrugs("1", "1")
