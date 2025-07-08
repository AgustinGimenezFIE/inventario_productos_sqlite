# 🧾 Sistema de Gestión de Inventario con SQLite

Este proyecto es parte del **Trabajo Final Integrador** del curso de Python – Comisión 25003, Turno Tarde, bajo la supervisión del profesor **Gabriel Feldman**.

---

## 📌 Descripción

Este sistema de consola en Python permite administrar un inventario de productos utilizando una base de datos SQLite. A diferencia de la pre-entrega (que usaba listas en memoria), esta versión utiliza persistencia real de datos.

El sistema permite:

- Agregar productos (nombre, descripción, cantidad, precio y categoría).
- Mostrar todos los productos registrados.
- Buscar productos por nombre.
- Eliminar productos por ID.
- Actualizar productos por ID.
- Generar un reporte de productos con bajo stock.

Los datos se almacenan en la base de datos `inventario.db`, la cual se crea automáticamente.

---

## ✅ Requisitos cumplidos

- ✅ Uso de SQLite y base de datos persistente.
- ✅ Modularización del código (`main.py`, `db.py`, `utils.py`, `config.py`).
- ✅ Interacción por consola clara y validada.
- ✅ Reporte personalizado de productos con bajo stock.
- ✅ Uso del módulo `colorama` para mejorar la experiencia en consola.
- ✅ Código comentado, limpio y mantenible.

---

## 🖥️ Cómo ejecutar el programa

1. Asegurate de tener **Python 3.x** instalado.
2. Cloná este repositorio:

```bash
git clone https://github.com/AgustinGimenezFIE/inventario_productos_sqlite.git
cd inventario_productos_sqlite

pip install -r requirements.txt

python main.py

========== Sistema de Inventario ==========
1. Agregar producto
2. Mostrar productos
3. Buscar producto por nombre
4. Eliminar producto por ID
5. Actualizar producto por ID
6. Reporte de bajo stock
7. Salir

Seleccione una opción: 1
Nombre: Lápiz
Descripción: Lápiz negro N°2
Cantidad: 20
Precio: 150
Categoría: Librería
✅ Producto agregado.

inventario_productos_sqlite/
├── main.py         # Menú principal
├── db.py           # Funciones para operar la base de datos
├── utils.py        # Funciones auxiliares (inputs, colores, etc.)
├── config.py       # Configuración (nombre de DB)
├── requirements.txt
└── inventario.db   # (Se crea automáticamente)
