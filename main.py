from db import *
from utils import *

def menu():
    print("\n" + "="*10 + " Sistema de Inventario " + "="*10)
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto por nombre")
    print("4. Eliminar producto por ID")
    print("5. Actualizar producto por ID")
    print("6. Reporte de bajo stock")
    print("7. Salir")

if __name__ == "__main__":
    crear_tabla()
    while True:
        menu()
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("⚠️ Opción inválida.")
            continue

        if opcion == 1:
            datos = solicitar_datos_producto()
            if datos:
                agregar_producto(*datos)
                print("✅ Producto agregado.")

        elif opcion == 2:
            mostrar_productos(listar_productos())

        elif opcion == 3:
            nombre = input("Ingrese nombre a buscar: ").strip()
            resultados = buscar_producto_por_nombre(nombre)
            mostrar_productos(resultados)

        elif opcion == 4:
            try:
                id = int(input("ID a eliminar: "))
                if eliminar_producto_por_id(id):
                    print("✅ Producto eliminado.")
                else:
                    print("❌ No se encontró ese ID.")
            except ValueError:
                print("⚠️ ID inválido.")

        elif opcion == 5:
            try:
                id = int(input("ID a actualizar: "))
                datos = solicitar_datos_producto()
                if datos and actualizar_producto(id, *datos):
                    print("✅ Producto actualizado.")
                else:
                    print("❌ No se pudo actualizar el producto.")
            except ValueError:
                print("⚠️ ID inválido.")

        elif opcion == 6:
            try:
                limite = int(input("Mostrar productos con cantidad <= a: "))
                mostrar_productos(productos_bajo_stock(limite))
            except ValueError:
                print("⚠️ Valor inválido.")

        elif opcion == 7:
            print("👋 Hasta luego.")
            break
        else:
            print("⚠️ Opción no válida.")
