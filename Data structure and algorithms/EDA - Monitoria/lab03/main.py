import sys
import random
import math
from datetime import datetime

import cVetor

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

    random.seed(int(datetime.now().strftime('%H%M%S')))

    if (len(sys.argv) > 1):
        n = int(sys.argv[1])
    else:
        n = 50

    v = cVetor.cVetor(n)
        
    for i in range(1, n // 2):
        v.insere(i)

    print(v.buscaBinRec(6))