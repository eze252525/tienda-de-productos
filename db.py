import sqlite3

def crear_tabla():
    conn = sqlite3.connect("inventario.db")
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
    conn.close()

def agregar_producto(nombre, descripcion, cantidad, precio, categoria):
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)",
        (nombre, descripcion, cantidad, precio, categoria)
    )
    conn.commit()
    conn.close()
    