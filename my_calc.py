def summa(a,b):
    return a+b
def raznost(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divade(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Can't divide by zero"