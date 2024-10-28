def checkvalidity(a, b, c):

    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False
    else:
        return True
    
    a = 7
    b = 10 
    c = 5

    if checkvalidity(a, b, c):
        print("Valid")
    else:
        print("invalid")