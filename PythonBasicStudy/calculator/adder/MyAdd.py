def add(num1, num2):
    return num1 + num2

def addMultiNum(*args):
    total = 1
    for i in args:
        total += i

    return total