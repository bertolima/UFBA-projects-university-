from Screen import *
from cSetor import*
import sys


if __name__ == '__main__':
    try:
        nSetores = int(sys.argv[1])
        screen = Screen(nSetores)
        screen.end()
    except:
        screen = Screen(10)
        screen.end()



