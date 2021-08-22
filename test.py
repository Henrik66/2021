def uwu(word):
    return word


def pog(str):
    return str*690

def xIntercepts(a, h, k):
    # y = a(x-h)^2 + k
    # (-k/a)^0.5 = x-h
    d = (-k/a)**(.5)
    x1 = h + d
    x2 = h-d
    return x1, x2


def waiter(food, drink, dessert):
    return "Okay, so you wanted " + str(food) + " and a " + str(drink) + " to drink with it!"
