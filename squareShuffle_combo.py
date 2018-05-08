# not very fast when len(ws) > 25ish
from itertools import combinations

def squareCheck(ws):
    if len(ws)%2 == 0:
        indws = list(range(len(ws)))
        for combo in combinations(indws, int(len(ws)/2)):
            xs = []
            ys = []
            for ind in indws:
                if ind in set(combo):
                    xs.append(ws[ind])
                else:
                    ys.append(ws[ind])
            if xs == ys:
                return True, xs
    return False

