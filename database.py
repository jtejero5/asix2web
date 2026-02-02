import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")

# Crear la base de datos si no existe
def init_db():
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        ''')
        conn.commit()
        conn.close()

# Obtener conexión a la BD
def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# Buscar email por nombre
def buscar_email(nombre):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'SELECT email FROM usuarios WHERE nombre = ?',
        (nombre,)
    )
    resultado = cursor.fetchone()
    conn.close()
    return resultado

# Agregar nuevo usuario
def agregar_usuario(nombre, email):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO usuarios (nombre, email) VALUES (?, ?)',
            (nombre, email)
        )
        conn.commit()
        conn.close()
        return True, "Usuario agregado correctamente"
    except sqlite3.IntegrityError:
        return False, "El email ya existe en la base de datos"
    except Exception as e:
        return False, f"Error: {str(e)}"
