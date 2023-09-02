import BureaucracyModel
import DoctorService
import BureaucraryService


class DoctorController():
    def __init__(self):
        self.arr1 = []  # Define arr1 as an instance variable

    def listAllPains(self):
        return DoctorService.DoctorService().getAllPainsList()

    def getOnePain(self, painId):
        DoctorService.DoctorService().getOnePain(painId)

    def addPain(self, painId):
        DoctorService.DoctorService().addPain(painId)

    def deleteOnePain(self, painId):
        DoctorService.DoctorService().deleteOnePain(painId)

    def assignmentDrugs(self, pain_id, drug_id):
        try:
            BureaucracyModel.BureaucracyModel().checkAssignment(pain_id, drug_id)
            BureaucracyModel.BureaucracyModel().writeAssignment(pain_id, drug_id)
        except Exception as e:
            print(e)
    
    def makeViscera(self, email):
        BureaucraryService.BureacracyService().makeViscera(email)

    def viewViscera(self, email):
        # print(email)
        BureaucraryService.BureacracyService().viewViscera(email)



qwa = DoctorController()
# qwa.AssignmentDrugs("1", "1")
# qwa.AssignmentDrugs("1", "1")
# qwa.addPain(1)
# qwa.addPain(2)
# qwa.addPain(3)DoctorService
# print(qwa.getOnePain(1))
# qwa.deleteOnePain(2)
# print(qwa.listAllPains())
# qwa.makeViscera("123@qwe.q")
qwa.viewViscera("123@qwe.q")
