from cHospital import Hospital
from cTADs import queue, stack, normalQueue
from cPacient import Patient
from cBed import Bed
import random
import time

class Simulator:
    def __init__(self):
        self.hospitals = []
        self.genHospitals()

        self.a = normalQueue()
        self.b = normalQueue()
        self.c = normalQueue()

        self.adult = queue()
        self.ped = queue()
        self.neo = queue()
        
        self.adultBed = stack()
        self.pedBed = stack()
        self.neoBed = stack()
        
        self.occuped = 0
        self.free = 0
        self.disPac = 0
        self.died = 0
        self.discharged = 0

    def genHospitals(self):
        for i in range(10):
            hospital = Hospital(str(i))
            self.hospitals.append(hospital)
            
    def fillQueues(self):
        for hospital in self.hospitals:
            x = random.randrange(1, 6, 1)
            for i in range(x):
                pacient = hospital.fillQueue()

                if pacient.getStage() > 2:
                    if pacient.getType() == 'Adult':
                        self.adult.insert(pacient)
                    elif pacient.getType() == 'Pediatric':
                        self.ped.insert(pacient)
                    elif pacient.getType() == 'Neonatal':
                        self.neo.insert(pacient)
        else:
            self.disPac += 1
                
    def fillStacks(self):
        for hospital in self.hospitals:
            x = random.randrange(1, 4, 1)
            for i in range(x):
                bed = hospital.fillStack()

                if bed.getType() == 'Adult':
                    self.adultBed.pull(bed)
                elif bed.getType() == 'Pediatric':
                    self.pedBed.pull(bed)
                elif bed.getType() == 'Neonatal':
                    self.neoBed.pull(bed)
                self.free += 1

    def allocate(self):
        while not self.adultBed.isEmpty():
            if self.adult.isEmpty():
                break
            pacient = self.adult.delete()
            bed = self.adultBed.getTop()
            self.adultBed.pop()
            bed.setPacient(pacient)
            self.a.set(bed)
            self.occuped += 1
            self.free -= 1

        while not self.pedBed.isEmpty():
            if self.ped.isEmpty():
                break
            pacient = self.ped.delete()
            bed = self.pedBed.getTop()
            self.pedBed.pop()
            bed.setPacient(pacient)
            self.a.set(bed)
            self.occuped += 1
            self.free -= 1
   
        while not self.neoBed.isEmpty():
            if self.neo.isEmpty():
                break
            pacient = self.neo.delete()
            bed = self.neoBed.getTop()
            self.neoBed.pop()
            bed.setPacient(pacient)
            self.a.set(bed)
            self.occuped += 1
            self.free -= 1
    
    def attPacinBed(self):
        while not self.a.isEmpty():
            bed = self.a.get()
            self.a.remove()
            if bed.isOccup():
                bed.attPacient()
                if bed.checkPacient() == 1:
                    self.died += 1
                    self.occuped -= 1
                elif bed.checkPacient() == 0:
                    self.discharged += 1
                    self.occuped -= 1
                bed.attBed()
            self.adultBed.pull(bed)
            
        while not self.b.isEmpty():
            bed = self.b.get()
            self.a.remove()
            if bed.isOccup():
                bed.attPacient()
                if bed.checkPacient() == 1:
                    self.died += 1
                    self.occuped -= 1
                elif bed.checkPacient() == 0:
                    self.discharged += 1
                    self.occuped -= 1
                bed.attBed()
            self.pedBed.pull(bed)
        
        while not self.c.isEmpty():
            bed = self.c.get()
            self.a.remove()
            if bed.isOccup():
                bed.attPacient()
                if bed.checkPacient() == 1:
                    self.died += 1
                    self.occuped -= 1
                elif bed.checkPacient() == 0:
                    self.discharged += 1
                    self.occuped -= 1
                bed.attBed()
            self.neoBed.pull(bed)

        
    def attInQueue(self):
        a = queue()
        while not self.adult.isEmpty():
            item = self.adult.remove()
            item.stageRand()
            if item.getStage() == 0:
                self.died += 1
            elif item.getStage() == 1 or item.getStage() == 2:
                self.disPac += 1
            else:
                a.insert(item)
        self.adult = a

        a = queue()
        while not self.ped.isEmpty():
            item = self.ped.remove()
            item.stageRand()
            if item.getStage() == 0:
                self.died += 1
            elif item.getStage() == 1 or item.getStage() == 2:
                self.disPac += 1
            else:
                a.insert(item)
        self.ped = a

        a = queue()
        while not self.neo.isEmpty():
            item = self.neo.remove()
            item.stageRand()
            if item.getStage() == 0:
                self.died += 1
            elif item.getStage() == 1 or item.getStage() == 2:
                self.disPac += 1
            else:
                a.insert(item)
        self.neo = a
        del a
        

    def getOccuped(self):
        return self.occuped
    def getFree(self):
        return self.free

    def getAdultB(self):
        return self.adultBed.getLen()
    def getPedB(self):
        return self.neoBed.getLen()
    def getNeoB(self):
        return self.neoBed.getLen()
    
    def getAdult(self):
        return self.adult.getLen()
    def getPed(self):
        return self.ped.getLen()
    def getNeo(self):
        return self.neo.getLen()
     
    def getAll(self):
        return self.adult.getLen() + self.ped.getLen() + self.neo.getLen()
    def getDied(self):
        return self.died
    def getDis(self):
        return self.disPac

    def getDischarged(self):
        return self.discharged

            


