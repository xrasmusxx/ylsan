a = float(input("sisesta esimene number: "))
b = float(input("sisesta teine number"))
c = float(input("sisesta kolmas number"))

if (a >= b) and (a >= c):
    largest = a

elif (b >= a) and (b >= c):
    largest = b
else:
    largest = c

    print("suurim number on: ", largest)