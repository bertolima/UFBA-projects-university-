import random

class Patient:
    def __init__(self, id, origin):
        self.id = id
        self.origin = origin
        self.age = None
        self.stage = None
        self.type = None
        self.setAge()
        self.setType()
        self.setStage()

    def setType(self):
        if self.age == 0:
            self.type = "Neonatal"
        elif self.age > 0 and self.age < 14:
            self.type = "Pediatric"
        elif self.age > 13 and self.age < 99:
            self.type = "Adult"
    def setAge(self):
        x = random.randrange(0, 10, 1)
        if x < 2:
            self.age = 0
        elif x >= 2 and x <= 5:
            self.age = random.randrange(1, 14, 1)
        elif x >= 6 and x <= 9:
            self.age = random.randrange(14, 100, 1)

    def setStage(self):
        x = random.randrange(0, 11, 1)
        if x == 0 or x == 1:
            self.stage = 5
        elif x == 2 or x == 3:
            self.stage = 4
        elif x == 4 or x == 5 or x == 6:
            self.stage = 3
        elif x == 7 or x == 8:
            self.stage = 2
        elif x == 9 or x== 10:
            self.stage = 1
    
    def stageRand(self):
        if self.stage == 1:
            x = random.randrange(0, 9, 1)
            if x == 0 or x == 1 or x == 2 or x == 3 or x == 5:
                self.stage = 1
            elif x == 6 or x == 7:
                self.stage = 2
            elif x == 8:
                self.stage = 3

        elif self.stage == 2:
            x = random.randrange(0, 9, 1)
            if x >= 0 and x <= 4:
                self.stage = 1
            elif x >= 5 and x <= 6:
                self.stage = 2
            elif x == 7:
                self.stage = 3
            elif x == 8:
                self.stage = 4

        elif self.stage == 3:
            x = random.randrange(0, 8, 1)
            if x == 0 or x == 1 or x == 2:
                self.stage = 3
            elif x == 3 or x == 4:
                self.stage = 4
            elif x == 5 or x == 6:
                self.stage = 2
            elif x == 8:
                self.stage = 5

        elif self.stage == 4:
            x = random.randrange(0, 8, 1)
            if x == 0 or x == 1:
                self.stage = 5
            elif x == 2 or x == 3:
                self.stage = 4
            elif x == 4 or x == 5 or x == 6:
                self.stage = 3
            elif x == 7:
                self.stage = 0

        elif self.stage == 5:
            x = random.randrange(0, 8, 1)
            if x == 0 or x == 1:
                self.stage = 0
            elif x == 2 or x == 3 or x == 4:
                self.stage = 5
            elif x == 5 or x == 6:
                self.stage = 4
            elif x == 7:
                self.stage = 3

    def getStage(self):
        return self.stage

    def getType(self):
        return self.type

