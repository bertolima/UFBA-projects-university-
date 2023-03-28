import pyglet
from pyglet.window.key import *
from pyglet import clock
from pyglet.window import key

def createLabel(name, x, y, text, fontSize):
    name.text = text
    name.x = x
    name.y = y
    name.font_size = fontSize

def simulaEvent(x):
    global cont
    cont = 0
    
    window = pyglet.window.Window(width=1280, height=720)

    pF = pyglet.text.Label(anchor_x='left', anchor_y='top')
    bO = pyglet.text.Label(anchor_x='left', anchor_y='top')
    pD = pyglet.text.Label(anchor_x='left', anchor_y='top')

    beds = pyglet.text.Label(anchor_x='left', anchor_y='top')
    createLabel(beds, window.width//3+200, window.height//1.5+70, "AVAILABLE BEDS", 20)
    bA = pyglet.text.Label(anchor_x='left', anchor_y='top')
    bP = pyglet.text.Label(anchor_x='left', anchor_y='top')
    bN = pyglet.text.Label(anchor_x='left', anchor_y='top')

    pacients = pyglet.text.Label(anchor_x='left', anchor_y='top')
    createLabel(pacients, window.width//3+200, window.height//1.5-130, "PATIENT QUEUE", 20)
    pA = pyglet.text.Label(anchor_x='left', anchor_y='top')
    pP = pyglet.text.Label(anchor_x='left', anchor_y='top')
    pN = pyglet.text.Label(anchor_x='left', anchor_y='top')

    pDied = pyglet.text.Label(anchor_x='left', anchor_y='top')
    pB = pyglet.text.Label(anchor_x='left', anchor_y='top')

    createLabel(pF, 0, window.height, "Patient Queue: "+ str(x.getAll()), 25)
    createLabel(bO, 400, window.height,"Occuped Beds: " + str(x.getOccuped()), 25)
    createLabel(pD, 800, window.height, "Discharged Patients: " + str(x.getDischarged()), 25)

    createLabel(bA, window.width//3, window.height//1.5, "Adult: "+ str(x.getAdultB()), 20)
    createLabel(bP, window.width//3+200, window.height//1.5, "Pediatric: "+ str(x.getPedB()), 20)
    createLabel(bN, window.width//3+400, window.height//1.5, "Neonatal: "+ str(x.getNeoB()), 20)

    createLabel(pA, window.width//3, window.height//1.5-200, "Adult: "+ str(x.getAdult()), 20)
    createLabel(pP, window.width//3+200, window.height//1.5-200, "Pediatric: "+ str(x.getPed()), 20)
    createLabel(pN, window.width//3+400, window.height//1.5-200, "Neonatal: "+ str(x.getNeo()), 20)

    createLabel(pDied, 0, 50, "Dead Patients: "+ str(x.getDied()), 20)
    createLabel(pB, 500, 50, "Patients that get better in queue: "+ str(x.getDis()), 20)


    def updatePoint(dt):
        global cont
        if cont == 1:
            x.fillQueues()
        elif cont == 2:
            x.fillStacks()
        elif cont == 3:
            x.allocate()
        elif cont == 4:
            x.attInQueue()
            cont = 0

        pF.text =  "Patient Queue: "+ str(x.getAll())
        bO.text =  "Occuped Beds: " + str(x.getOccuped())
        pD.text =  "Discharged Patients: " + str(x.getDischarged())

        bA.text =  "Adult: "+ str(x.getAdultB())
        bP.text =  "Pediatric: "+ str(x.getPedB())
        bN.text =  "Neonatal: "+ str(x.getNeoB())

        pA.text =  "Adult: "+ str(x.getAdult())
        pP.text =  "Pediatric: "+ str(x.getPed())
        pN.text =  "Neonatal: "+ str(x.getNeo())

        pDied.text =  "Dead Patients: "+ str(x.getDied())
        pB.text =  "Patients that get better in queue: "+ str(x.getDis())
        cont += 1

    @window.event
    def on_key_press(symbol, modifiers):
        if symbol == key.S:

            print('The "S" key was pressed.')
            for j in range(0,1000, 2):
                clock.schedule_once(updatePoint, j)

    @window.event
    def on_draw():
        window.clear()
        pF.draw()
        bO.draw()
        pD.draw()

        beds.draw()
        bA.draw()
        bP.draw()
        bN.draw()

        pacients.draw()
        pA.draw()
        pP.draw()
        pN.draw()
        
        pDied.draw()
        pB.draw()


    pyglet.app.run()