from Swap import Swap

test_in = "S,T,C"
test_out = [["T","S"],["T","S"],["C","C"]]

instructions = []

OUTSIDE = 0
KEYS = 1



LEFT = 0
MID = 1
RIGHT = 2
#######################################################################
def solve(inside, outside, challenge):
    CONTINUE = True
    escape = findKey(inside,challenge)
    print("Escape Shapes: "+str(escape))
    while CONTINUE:
        mismatch = identifyIncorrectShapes(outside,escape)
        swaps = findSwaps(mismatch)
        if len(swaps) == 0:
            CONTINUE = False
        performSwap(swaps, outside)
    return instructions


#######################################################################
def findKey(inside,challenge):

    escape = None

    ins_list = inside.split(",")
    if challenge:
        escape = ins_list[-1:] + ins_list[:-1]
        for x in range(3):
            escape[x] = [escape[x],escape[x]]

        return escape

    else:
        escape = []
        for x in range(3):
            if ins_list[x] == "T":
                escape.append(["C","S"])
            elif ins_list[x] == "C":
                escape.append(["T","S"])
            elif ins_list[x] == "S":
                escape.append(["T","C"])
        return escape
#######################################################################
def identifyIncorrectShapes(outside, key):
    mismatch = []
    for x in range(3):
        statue = []
        for y in range(2):
            if not(outside[x][y] == key[x][y]):
                statue.append([outside[x][y],key[x][y]])
        mismatch.append(statue)

    return mismatch
#######################################################################
def findSwaps(mismatch):
    swaps = []
    for x in range(3):
        for wrong in mismatch[x]:
            for y in range(3):
                if x == y:##if were comparing the same statue
                    continue
                for otherwrong in mismatch[y]:
                    if wrong[1] == otherwrong[0]:
                        perfect = False
                        if wrong[0] == otherwrong[1]:
                            perfect = True
                        swaps.append(Swap(wrong[0],x,otherwrong[0],y,perfect))

    return swaps

#######################################################################

def performSwap(swaps, outside):
    global instructions
    if len(swaps) == 0:
        return
    perfectSwaps = [swap for swap in swaps if swap.perfect == True]
    selected = None
    if len(perfectSwaps) > 0:
        selected = perfectSwaps[0]
    else:
        selected = swaps[0]
    outside[selected.targetPos][outside[selected.targetPos].index(selected.targetShape)] = selected.originShape
    outside[selected.originPos][outside[selected.originPos].index(selected.originShape)] = selected.targetShape
    instructions.append(selected)
#######################################################################
