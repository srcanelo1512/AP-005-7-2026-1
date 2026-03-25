import os  # Para limpiar la pantalla

# ----------- FUNCIÓN PARA LIMPIAR PANTALLA ----------
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

# ----------- TUPLA: CATEGORÍAS FIJAS ----------------
CATEGORIAS = (
    "Partes del auto",
    "Neumáticos",
    "Electrónica",
    "Merchandising",
    "Herramientas de pit stop"
)

# ----------- LISTA PARA GUARDAR PRODUCTOS -----------
inventario_f1 = []

# ----------- MENSAJE DE BIENVENIDA ------------------}

limpiar_pantalla()
print("==============================================")
print("   BIENVENIDO AL SISTEMA DE INVENTARIO F1 🏎️")
print("==============================================")

# ----------- FUNCIÓN PARA MOSTRAR MENÚ --------------
def mostrar_menu():
    print("\nMenú principal")
    print("1. Agregar producto F1")
    print("2. Mostrar inventario")
    print("3. Buscar producto por código")
    print("4. Eliminar producto")
    print("5. Salir")

# ----------- CICLO PRINCIPAL ------------------------
opcion = 0

while opcion != 5:
    mostrar_menu()

    # Conversión de tipo
    opcion = int(input("\nSeleccione una opción: "))
    limpiar_pantalla()   # ← LIMPIA CADA VEZ QUE CAMBIA LA OPCIÓN

    # ----------- OPCIÓN 1: AGREGAR PRODUCTO ----------
    if opcion == 1:
        print("--- Agregar producto de Fórmula 1 ---")

        codigo = input("Código del producto: ")

        codigo_repetido = False
        for producto in inventario_f1:
            if producto["codigo"] == codigo:
                codigo_repetido = True

        if codigo_repetido:
            print("Ese código ya existe.")
        else:
            nombre = input("Nombre del producto: ")

            precio = float(input("Precio: "))      # Conversión float
            cantidad = int(input("Cantidad: "))    # Conversión int

            print("\nCategorías disponibles:")
            for i in range(len(CATEGORIAS)):
                print(i + 1, ".", CATEGORIAS[i])

            categoria_opcion = int(input("Seleccione la categoría: "))

            if categoria_opcion < 1 or categoria_opcion > len(CATEGORIAS):
                print("Categoría no válida.")
            else:
                categoria = CATEGORIAS[categoria_opcion - 1]

                producto_f1 = {
                    "codigo": codigo,
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad,
                    "categoria": categoria
                }

                inventario_f1.append(producto_f1)
                print("Producto agregado correctamente.")

    # ----------- OPCIÓN 2: MOSTRAR INVENTARIO --------
    elif opcion == 2:
        print("--- Inventario Fórmula 1 ---")

        if len(inventario_f1) == 0:
            print("No hay productos registrados.")
        else:
            for producto in inventario_f1:
                print("-----------------------------")
                print("Código:", producto["codigo"])
                print("Nombre:", producto["nombre"])
                print("Precio:", producto["precio"])
                print("Cantidad:", producto["cantidad"])
                print("Categoría:", producto["categoria"])

    # ----------- OPCIÓN 3: BUSCAR PRODUCTO -----------
    elif opcion == 3:
        codigo_buscar = input("Código del producto: ")
        encontrado = False

        for producto in inventario_f1:
            if producto["codigo"] == codigo_buscar:
                print("Producto encontrado:")
                print(producto)
                encontrado = True

        if not encontrado:
            print("Producto no encontrado.")

    # ----------- OPCIÓN 4: ELIMINAR PRODUCTO ---------
    elif opcion == 4:
        codigo_eliminar = input("Código del producto a eliminar: ")
        eliminado = False

        for producto in inventario_f1:
            if producto["codigo"] == codigo_eliminar:
                inventario_f1.remove(producto)
                eliminado = True
                print("Producto eliminado.")

        if not eliminado:
            print("Producto no encontrado.")

    # ----------- OPCIÓN 5: SALIR --------------------
    elif opcion == 5:
        print("Saliendo del sistema... 🏁")

    else:
        print("Opción no válida.")

    input("\nPresione ENTER para continuar...")
    limpiar_pantalla()
