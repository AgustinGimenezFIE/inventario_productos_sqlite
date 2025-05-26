# main.py
#  Agustin Hugo Gimenez
#  5/2025 - Talento Tech 25003 Turno Tarde

opcion = 0
productos = []

while opcion != 5:
    print("\nSistema de Gestión Básica De Productos\n")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir\n")

    try:
        opcion = int(input("Ingrese una opción: "))
    except ValueError:
        print("⚠️ Opción inválida. Por favor, ingrese un número del 1 al 5.")
        continue

    if opcion == 1:
        print("\n🛒 Agregar producto")
        nombre = input("Ingrese el nombre del producto: ").strip()
        categoria = input("Ingrese la categoría del producto: ").strip()
        try:
            precio = int(input("Ingrese el precio del producto (sin centavos): "))
        except ValueError:
            print("⚠️ Precio inválido. Debe ser un número entero.")
            continue

        if nombre and categoria:
            producto = [nombre, categoria, precio]
            productos.append(producto)
            print("✅ Producto agregado con éxito.")
        else:
            print("⚠️ No se permiten campos vacíos.")

    elif opcion == 2:
        print("\n📋 Lista de productos registrados\n")
        if productos:
            for i in range(len(productos)):
                print(f"{i}. Nombre: {productos[i][0]} | Categoría: {productos[i][1]} | Precio: ${productos[i][2]}")
        else:
            print("No hay productos registrados.")

    elif opcion == 3:
        print("\n🔍 Buscar producto")
        buscar = input("Ingrese el nombre del producto a buscar: ").strip().lower()
        encontrados = False

        for i, producto in enumerate(productos):
            if producto[0].lower() == buscar:
                print(f"{i}. Nombre: {producto[0]} | Categoría: {producto[1]} | Precio: ${producto[2]}")
                encontrados = True

        if not encontrados:
            print("❌ El producto no fue encontrado.")

    elif opcion == 4:
        print("\n🗑️ Baja de producto")
        try:
            indice = int(input("Ingrese el número de producto a eliminar: "))
            if 0 <= indice < len(productos):
                eliminado = productos.pop(indice)
                print(f"✅ Producto '{eliminado[0]}' eliminado.")
            else:
                print("⚠️ El número de producto no existe.")
        except ValueError:
            print("⚠️ Entrada inválida. Debe ser un número.")

    elif opcion == 5:
        print("👋 Gracias por usar nuestra aplicación.")
    else:
        print("⚠️ Opción Incorrecta.")
