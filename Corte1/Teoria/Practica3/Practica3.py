while True: 
    a = input("por favor ingrese un valor: ")

    aint = int(a)

    mod = aint%2

    if (mod == 0):
        print("el numero es par: ")
    else:
        print("el numero es impar: ")

    b = input("si desea salir del programa digite E sino cualquier otra tecla: ")

    if (b == "e"):
        print("gracias por utilizar el programa ")
        break
