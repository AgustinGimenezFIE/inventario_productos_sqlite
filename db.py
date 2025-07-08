import sqlite3
from config import DB_NAME

def conectar_db():
    return sqlite3.connect(DB_NAME)

def crear_tabla():
    with conectar_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL,
                categoria TEXT
            )
        ''')
        conn.commit()

def agregar_producto(nombre, descripcion, cantidad, precio, categoria):
    with conectar_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
            VALUES (?, ?, ?, ?, ?)
        ''', (nombre, descripcion, cantidad, precio, categoria))
        conn.commit()

def listar_productos():
    with conectar_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")
        return cursor.fetchall()

def buscar_producto_por_nombre(nombre):
    with conectar_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", ('%' + nombre + '%',))
        return cursor.fetchall()

def eliminar_producto_por_id(id):
    with conectar_db() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
        conn.commit()
        return cursor.rowcount

def actualizar_producto(id, nombre, descripcion, cantidad, precio, categoria):
    with conectar_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE productos
            SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
            WHERE id = ?
        ''', (nombre, descripcion, cantidad, precio, categoria, id))
        conn.commit()
        return cursor.rowcount

def productos_bajo_stock(limite):
    with conectar_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
        return cursor.fetchall()
