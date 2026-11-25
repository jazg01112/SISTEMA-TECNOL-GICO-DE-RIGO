import sqlite3

RUTA_BD = "database.db"

def conectar():
    return sqlite3.connect(RUTA_BD)

def crear_tabla():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            categoria TEXT NOT NULL,
            marca TEXT NOT NULL,
            precio REAL NOT NULL,
            existencia INTEGER NOT NULL
        )
    """)
    conexion.commit()
    conexion.close()

def obtener_productos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT id, nombre, categoria, marca, precio, existencia
        FROM productos ORDER BY id
    """)
    productos = cursor.fetchall()
    conexion.close()
    return productos

def insertar_producto(producto):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO productos (id, nombre, categoria, marca, precio, existencia)
        VALUES (?, ?, ?, ?, ?, ?)
    """, producto)
    conexion.commit()
    conexion.close()

def obtener_producto(id_producto):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT id, nombre, categoria, marca, precio, existencia
        FROM productos WHERE id = ?
    """, (id_producto,))
    producto = cursor.fetchone()
    conexion.close()
    return producto

def eliminar_producto(id_producto):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
    eliminados = cursor.rowcount
    conexion.commit()
    conexion.close()
    return eliminados
