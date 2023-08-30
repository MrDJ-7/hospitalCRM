class RoomsModel:
    def __init__(self):
        self.arr1 = []  # Define arr1 as an instance variable

    def listAllRooms(self, arr):
        self.arr1 = arr  # Assign arr to the instance variable arr1
        return self.arr1

    def getOneRoom(self, index):
        if 0 <= index < len(self.arr1):  # Check if the index is within bounds
            return self.arr1[index]
        else:
            return None  # Return None if the index is out of bounds
