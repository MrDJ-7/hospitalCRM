import collections

class DrugsModel:
    def __init__(self):
        self.arr1 = []  # Define arr1 as an instance variable

    def listAllDrugs(self, arr):
        self.arr1 = arr  # Assign arr to the instance variable arr1
        return self.arr1

    def getOneDrug(self, index):
        if 0 <= index < len(self.arr1):  # Check if the index is within bounds
            return self.arr1[index]
        else:
            return None  # Return None if the index is out of bounds

# Create an instance of the DrugsModel class
# qwa = DrugsModel()
#
# # Define a list of drug dictionaries
# a1 = {'id': '24', 'name': 'noshpa'}
# a2 = {'id': '21', 'name': 'aspirin'}
# a3 = {'id': '32', 'name': 'nixar'}
# a = [a1, a2, a3]
#
# # Call the listAllDrugs method to populate the arr1 instance variable
# qwa.listAllDrugs(a)
#
# # Use the getOneDrug method to retrieve a drug by index
# print(qwa.listAllDrugs(a))
# print(qwa.getOneDrug(2))  # Output: {'id': '32', 'name': 'nixar'}
