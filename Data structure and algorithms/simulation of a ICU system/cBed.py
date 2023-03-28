import random

class Bed:
    def __init__(self, id, origin):
        self.id = id
        self.type = None
        self.origin = origin
        self.setType()

        self.occuped = False
        self.pacient = None

    def setType(self):
        x = random.randrange(0, 10, 1)
        if x < 2:
            self.type = 'Neonatal'
        elif x >= 2 and x <=5:
            self.type = 'Pediatric'
        elif x > 5 and x < 10:
            self.type = 'Adult'
    def getType(self):
        return self.type
    
    def setPacient(self, pacient):
        self.pacient = pacient
        self.occuped = True
    
    def attPacient(self):
        if self.isOccup():
            self.pacient.stageRand()
    
    def checkPacient(self):
        if self.pacient.getStage() == 0:
            return 1
        elif self.pacient.getStage() == 1 or self.pacient.getStage() == 2:
            return 0


    def attBed(self):
        if self.checkPacient() == 1 or self.checkPacient() == 0:
            self.occuped = False
            self.pacient = None
            return
        else:
            return
    def isOccup(self):
        if self.occuped is False:
            return False
        return True
        
        



