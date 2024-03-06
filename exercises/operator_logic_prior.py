alimento = True
dinero = True
_PUEDE = "PUEDE"
_NO_PUEDE = "NO PUEDE"
iterator = 0

while iterator < 4:
    if iterator == 0:
        if alimento or dinero:
            print(_PUEDE)
        else:
            print(_NO_PUEDE)
    elif iterator == 1:
        alimento = False
        if alimento or dinero:
            print(_PUEDE)
        else:
            print(_NO_PUEDE)
    elif iterator == 2:
        alimento = True
        dinero = False
        if alimento or dinero:
            print(_PUEDE)
        else:
            print(_NO_PUEDE)
    elif iterator == 3:
        alimento = False
        dinero = False
        if alimento or dinero:
            print(_PUEDE)
        else:
            print(_NO_PUEDE)

    iterator += 1

""" 
if m or not l and n:
    print("n is type: ", type(n), "and its value is: ", n)
lista = [12, "tres", True, 2.23]

for l in lista:
    print(l) """