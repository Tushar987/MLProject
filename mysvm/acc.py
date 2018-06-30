
import numpy as np

def get(res,tes):
    n = len(res)
    truth = (res == tes)
    pre = 0
    for i in truth:
        if i == True:
            pre += 1
    return (pre * 100) /n 

