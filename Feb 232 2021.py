#coding bat fun functions

def sum_double(a, b):
  if a == b:
    return (a+b)*2
  else:
    return (a+b)

def makes10(a, b):
    if a == 10 or b == 10 or a + b == 10:
        return True
    else:
        return False

def not_string(str):
    if len(str) >=3 and str[:3] == "not":
        return str
    else:
        return "not " + str
  
def near_hundred(n):
    if (abs(100-n) <= 10) or (abs(200-n) <= 10):
        return True
    else:
        return False

def diff21(n):
    if (abs(21-n) <= 21):
        return abs(21-n)
    else:
        return (abs(21-n))*2

def sum2(nums):
    if len(nums) >= 2:
        return(nums[0] + nums[1])
    else:
        return "undefined"


def sum3(nums):
    if len(nums) >= 3:
        return(nums[0] + nums[1] + nums[2])
    else:
        return "undefined"







