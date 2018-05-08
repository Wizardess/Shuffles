# This implementation is not robust against highly repetitive strings
# like binary, unfortunately.

# Finds a minimum value j > i such that w[i] = w[j], j not in set B
def findj(ws, i, j, B):
    newj = -1
    for x in range(j, len(ws)):
        if x not in B and ws[i] == ws[x]:
            newj = x
            break
    return newj

def helper(ws, i, j, B):
    j = findj(ws, i, j, B)
    for x in B:
        if x > i and x < j:
            helper(ws, i, j+1, B)
    return j

# This approach identifies matching elements in ws and `sorts` them into
    # lists x and y. To ensure index (in ws) for elements of y always
    # increases, we track the index (in ws) of the last item appended to y
    # as k. Finally, we track indices of ws added to y in set B so that we
    # do not add these elements to x.
    # NOTE: In line 27, `j >= 0` is necessary due to construction of findj
    # NOTE: By line 32, we should only have j > k left
    # NOTE: In line 36, we have x==y as a precaution
def squareCheck(ws):
    x = []
    y = []
    k = -1
    B = set()
    for i in range(len(ws)):
        if i in B:
            j = helper(ws, i, i+1, B)
            if j != -1:
                B.remove(i) 
                B.add(j)
        if i not in B:
            j = findj(ws, i, i+1, B)
            while j <= k and j >= 0:
                j = findj(ws, i, j+1, B)
            if j == -1:
                return False, x, y
            else:
                x.append(ws[i])
                y.append(ws[j])
                k = j
                B.add(j)
    return x==y, "".join(x)


testcase = "nneevveerr  ggoonnaa  ggiivvee  yyoouu  uupp"

print(squareCheck(testcase))
