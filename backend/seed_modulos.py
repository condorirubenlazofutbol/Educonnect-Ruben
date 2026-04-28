import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def seed_data():
    try:
        db_url = os.getenv("DATABASE_URL")
        connection = psycopg2.connect(db_url) if db_url else psycopg2.connect(
            host=os.getenv("DB_HOST","localhost"), user=os.getenv("DB_USER","postgres"),
            password=os.getenv("DB_PASSWORD","root"), dbname=os.getenv("DB_NAME","educonnect_ruben")
        )
        cursor = connection.cursor()

        # ── Importar seguridad de forma robusta ──
        try:
            import security as auth
        except ImportError:
            import sys
            sys.path.append(os.path.dirname(os.path.abspath(__file__)))
            import security as auth

        # ── Usuarios por defecto ──
        usuarios_default = [
            ("Admin",     "EduConnect", "admin@educonnect.com",    "Admin2026!",    "administrador", None),
            ("Profesor",  "Demo",       "profesor@educonnect.com", "Profesor2026!", "profesor",      "Básico"),
            ("Estudiante","Demo",       "estudiante@educonnect.com","Estud2026!",   "estudiante",    "Básico"),
        ]

        print("Iniciando creación de usuarios...")
        for nombre, apellido, email, password, rol, nivel in usuarios_default:
            cursor.execute("SELECT id FROM usuarios WHERE email=%s", (email,))
            if not cursor.fetchone():
                hashed = auth.get_password_hash(password)
                cursor.execute(
                    "INSERT INTO usuarios (nombre, apellido, email, password, rol, nivel_asignado) VALUES (%s,%s,%s,%s,%s,%s)",
                    (nombre, apellido, email, hashed, rol, nivel)
                )
                print(f"Creado: {email}")
            else:
                print(f"Ya existe: {email}")

        # ── Malla curricular (solo si no existe) ──
        cursor.execute("SELECT COUNT(*) FROM modulos")
        total_actual = cursor.fetchone()[0]
        
        if total_actual == 0:
            MALLA = [
                ("1er SEMESTRE - BÁSICO", "Básico", ["Introducción a la Informática", "Pensamiento Computacional", "Lógica de Programación I", "Algoritmos I", "Ofimática Básica"]),
                ("2do SEMESTRE - AUXILIAR", "Auxiliar", ["Sistemas Operativos", "Programación Básica", "Hardware Esencial", "Redes Locales", "Base de Datos Básica"]),
                ("3er SEMESTRE - MEDIO I", "Medio", ["Programación Intermedia", "Diseño Web I", "Base de Datos Intermedia", "Inglés Técnico I", "Emprendimiento Digital"]),
                ("4to SEMESTRE - MEDIO II", "Medio", ["Programación Web", "Diseño Web II", "Redes Intermedias", "Programación Móvil I", "Proyecto Integrador I"]),
                ("5to SEMESTRE - SUPERIOR I", "Superior", ["Arquitectura de Software", "Bases de Datos Avanzadas", "DevOps & Cloud", "Seguridad Informática", "Inglés Técnico II"]),
                ("6to SEMESTRE - SUPERIOR II", "Superior", ["Inteligencia Artificial", "Desarrollo Full Stack", "Gestión de Proyectos TI", "Programación Móvil II", "Proyecto Integrador II"]),
                ("7mo SEMESTRE - INGENIERÍA I", "Ingeniería", ["Fundamentos de Ing. de Software", "Matemáticas Discretas", "Arquitecturas de Computadoras", "Cálculo para Ingeniería"]),
                ("8vo SEMESTRE - INGENIERÍA II", "Ingeniería", ["Estructuras de Datos", "Sistemas Operativos Avanzados", "Compiladores", "Redes Avanzadas"]),
                ("9no SEMESTRE - INGENIERÍA III", "Ingeniería", ["Ingeniería de Datos", "Machine Learning Avanzado", "Ciberseguridad Avanzada", "Sistemas Distribuidos"]),
                ("10mo SEMESTRE - INGENIERÍA IV", "Ingeniería", ["Proyecto de Grado I", "Proyecto de Grado II", "Innovación y Tecnología", "Liderazgo y Gestión TI"])
            ]

            orden = 1
            for sub, niv, mods in MALLA:
                for m in mods:
                    cursor.execute("INSERT INTO modulos (nombre, nivel, subnivel, orden) VALUES (%s, %s, %s, %s) RETURNING id", (m, niv, sub, orden))
                    m_id = cursor.fetchone()[0]
                    orden += 1
                    for t in range(1, 5):
                        cursor.execute("INSERT INTO contenidos (modulo_id, tipo, titulo, url, tema_num) VALUES (%s, 'teoria', %s, '', %s)", (m_id, f"Tema {t}", t))
            connection.commit()
            return orden - 1
        
        connection.commit()
        return 0

    except Exception as e:
        print(f"Error: {e}")
        return str(e)
    finally:
        if 'connection' in locals() and connection:
            cursor.close(); connection.close()

if __name__ == "__main__":
    seed_data()
