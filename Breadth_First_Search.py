import numpy as np
import pandas as pd

def ParcoursLargeur(matrice, s):
    elm = s
    k = 0
    cue = []
    print(len(matrice[0]))
    for i in range(len(matrice[0])):
        mydect[i] = -1
    while k < len(matrice[0]):
        for i in range(len(matrice[0])):
            if matrice[elm, i] != 0:
                if mydect[i] == -1:
                    cue.insert(0, i)
                mydect[elm] = 1
                mydect[i] = 1

        print("----------------------------------------------------------------------------------------------------------")
        print(pd.Series(mydect))
        print(cue)
        print("----------------------------------------------------------------------------------------------------------")

        elm = cue[-1]
        print("elem = ", elm)
        if (len(cue)>1):
            del cue[-1]

        print(cue)
        k += 1




mydect = {}
connection = {}
matrice = np.array([
    [0,1,0,1,0,0,0,0,1],
    [1,0,0,0,0,0,0,1,0],
    [0,0,0,1,0,1,0,1,0],
    [1,0,1,0,1,0,0,0,0],
    [0,0,0,1,0,0,0,0,1],
    [0,0,1,0,0,0,1,0,0],
    [0,0,0,0,0,1,0,0,0],
    [0,1,1,0,0,0,0,0,0],
    [1,0,0,0,1,0,0,0,0]
])
long = len(matrice[0])

ParcoursLargeur(matrice, 0)