import random
import math

def makeShuffle(a,b):
    w = []
    x = list(a)
    y = list(b)
    while x and y:
        n = random.randint(1,3)
        if n == 1:
            m = random.randint(0, math.ceil(.05*len(x)))
            i = 0
            for i in range(0,m):
                w.append( x.pop(0) )
        else:
            m = random.randint(0, math.ceil(.05*len(y)))
            for i in range(0,m):
                w.append( y.pop(0) )
    if x: w = w + x
    if y: w = w + y
    return "".join(w)


a = "Jane"
b = "Seungju"

print(makeShuffle(a,b))