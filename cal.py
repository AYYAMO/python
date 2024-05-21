import numbers


def add(a,b):
    return a+b

def sub(a,b):
    return a-b
def multi(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a%b

def passwordcheck(password):
    if len(password)<7:
        print("the pasword has to be more than or equal to 7 digit")
    else:
        print("the account has been created")







