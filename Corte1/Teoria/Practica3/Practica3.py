while True: 
    a = input("por favor ingrese un valor: ")

    aint = int(a)

    mod = aint%2

    if (mod == 0):
        print("el numero es par: ")
    else:
        print("el numero es impar: ")

    b = input("si desea continuar con otro numero digite 1 sino 0: ")
   
    bint=int(b)

    if (bint == 0):
        break
