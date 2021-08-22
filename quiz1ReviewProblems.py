# quiz1ReviewProblems.py
# Name: 
# Date: 2/24/2021


# Returns the [x, y] coordinates of the vertex for a parabola
# in standard form, y = a*x**2 + b*x + c.
def findVertex(a, b, c):
    return None



# Takes in three True/False values, which indicates whether 
# each monkey is smiling or not. Returns False if no monkeys
# are smiling, or if exactly two monkeys are smiling (they
# wouldn't leave out one monkey from the trouble). Returns
# True if only one monkey is smiling (stirring up trouble
# alone) or if all three monkeys are smiling (stirring up
# trouble together).
def tripleTrouble(monkey1, monkey2, monkey3):
  return monkey1 ^ monkey2 ^ monkey3


# Determines the two x-intercepts of a quadratic equation
# that is written in vertex form:
# y = a(x-h)**2 + k
def xInterceptsFromVertexForm(a, h, k):
    pass



# Returns the number of even numbers submitted.
def howManyAreEven(a, b, c):
  return (a+1)%2 + (b+1)%2 + (c+1)%2

# first attempt version
def howManyAreEven2_(a, b, c):
  even = []
  if (a % 2) == 0:
   even.append(a)
  if (b % 2) == 0:
    even.append(b)
  if (c % 2) == 0:
    even.append(c)
  return len(even)



# Calculates the TOTAL value of an account under SIMPLE
# interest, starting with principle p, interest rate r, and
# duration t.
def simpleIntFormula(p, r, t):
  return p * (1 + (r * t))



# Calculates the TOTAL value of an account under COMPOUND
# interest, starting with principle p, interest rate r, and
# duration t.
def compoundIntFormula(p, r, t):
    return None



# Returns the number of x-intercepts of a parabola, given the
# standard-form quadratic equation y = a*x**2 + b*x + c.
def HowManyXIntercepts(a, b, c):
    return None



# Takes a temperature in farenheit and returns the equivalent
# temperature in celsius.
def farenToCels(f):
  return  (f - 32) * 5/9




