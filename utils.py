from colorama import Fore, Style, init
init(autoreset=True)

def mostrar_productos(productos):
    if not productos:
        print(Fore.YELLOW + "No hay productos para mostrar.")
        return
    for p in productos:
        print(f"{p[0]}. {p[1]} | {p[2]} | Cant: {p[3]} | Precio: ${p[4]:.2f} | Cat: {p[5]}")

def solicitar_datos_producto():
    nombre = input("Nombre: ").strip()
    descripcion = input("Descripción: ").strip()
    try:
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))
    except ValueError:
        print(Fore.RED + "Cantidad o precio inválido.")
        return None
    categoria = input("Categoría: ").strip()
    return nombre, descripcion, cantidad, precio, categoria
