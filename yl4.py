def minimum(a, b):

    if a <= b:
        return a
    else:
        return b
    a = float(input("sisesta esimene number"))
    b = float(input("sisesta teine number"))
    print("väiksem arv on: ")
    print(minimum(a, b))
    