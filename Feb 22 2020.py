# positions in the list matter

def createLineSI(s, yi):
    return [s, yi]

def createLinePS(x, y, s):
    yi = -s*x+y
    return [s, yi]

def createLine2P(x1, y1, x2, y2):
    return None

def createLineST(a, b, c):
    # ax + by = c
    return None


def getYInt(line):
    return line[1]

def getSlope(line):
    return line[0]

def getXInt(line):
    return -line[1]/line[0]

def getXInt2(line):
    return -getYInt(line)/getSlope(line)

def areParallel(lineA, lineB):
    if getSlope(lineA) == getSlope(lineB):
        return True
    else:
        return False

######################################
#
# Test Block
#
######################################

line1 = createLinePS(1, 1, 4)
line2 = createLineSI(4, 2)

print(str(getSlope(line2)))

print(str(getYInt(line2)))

print(str(getXInt(line2)))

print(str(getXInt2(line2)))


