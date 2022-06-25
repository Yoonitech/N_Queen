import numpy as np
import random
from timeit import default_timer as timer
from collections import deque
from numba import jit
import numba as nb
from queue import LifoQueue



# @nb.njit()
def Backtrack(AR, Column, N_Queen):
    Row_D = AR[Column]
    while (Row_D + 1) == (N_Queen):
        AR[Column] = -1
        Column = Column - 1
        Row_D = AR[Column]
        

    return Column    
# @nb.njit()
def Check_Row(AR, Column):
    Row = AR[Column]
    for i in range(Column):
        if AR[i] == Row:
            return False
    return True

# @nb.njit()
def Check_X(AR, Column, N_Queen):
    Row = AR[Column]
    R = Row
    C = Column
    for i in range(N_Queen):
        R += 1
        C -= 1
        if R == AR[C] and C >= 0:
            return False
    R = Row      
    C = Column  
    for i in range(N_Queen):
        R -= 1
        C -= 1
        if R == AR[C] and R != -1 and C >= 0:
            return False
    return True   

def Run_Alg(N_Queen):
    AR = []
    for i in range(N_Queen):
        AR.append(-1)
    t1 = timer()    

    Column = 0
    while(Column != N_Queen):

        if AR[Column] == -1:
            AR[Column] += 1

        while(Check_Row(AR, Column) != True or Check_X(AR, Column, N_Queen) != True):
            AR[Column] += 1
            if AR[Column] == (N_Queen):
                AR[Column] = -1
                
                Column = Backtrack(AR, (Column - 1), N_Queen)
                
                AR[Column] += 1                  
        Column += 1
    return (AR, round(timer() - t1,4))

