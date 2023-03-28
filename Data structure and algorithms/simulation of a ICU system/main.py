from inTerminal import runningMap
from cSimulator import Simulator
from cWindow_Core import simulaEvent
import pyglet

running = True
def stopRunning():   
    if running:
        running = False

x = Simulator()
try:
    #width and height must be equal  
    simulaEvent(x)

except:
    while running:
        runningMap(x)
