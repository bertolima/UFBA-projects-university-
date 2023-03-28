from cTADs import queue, stack, normalQueue
from cPacient import Patient
from cBed import Bed

class Hospital:
    def __init__(self, name):
        self.name = name
        self.pacID = -1
        self.bedID = -1
        
    def fillQueue(self):
        self.pacID += 1
        return Patient(self.pacID, self.name)
        
    def fillStack(self):
        if self.bedID <= 500:
            self.bedID += 1
            return Bed(self.bedID, self.name)  