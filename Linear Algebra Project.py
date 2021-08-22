# Linear Algebra Project


#Line function
#y = mx + b

# (x, y)

def createLine(s, yi):
    return [s, yi]


#value function

def yi(line):
    return line[1]

def slope(line):
    return line[0]

def xi(line):
    return -line[1]/line[0]


#fun functions part 4

def areParallel(lineA, lineB):
    if slope(lineA) == slope(lineB):
        return True
    else:
        return False
def arePerpendicular(lineA, lineB):
    if slope(lineA) == -1/slope(lineB):
        return True
    else:
        return False

def evaluate(x, line):
    result = (line[0] * x) + line[1]
    return result

def reverse(y, line):
    result = y - (line[1] * line[0])
    return result

def fancyPrint(line):
    result = print("y = " + str(line[0]) + "x " + str(line[1]))
    return result

def whichQuadrants(line):
    if slope(line) >0:
        if yi(line) >0:
            return [1, 2, 3]
        elif yi(line) == 0:
            return[1, 3]
        else:
            return[1, 3, 4]
    


#def whichQuadrants(line):
#    if xi(line) > 0 and yi(line) > 0
 #       retur
  #  if xi(line) > 0 and yi(line) < 0
   #     return 4
   # if xi(line) < 0 and yi(line) < 0
   #     return 3
   # if xi(line) < 0 and yi(line) > 0
   #     return 2
   # return undefined

line = createLine(2, 2)




