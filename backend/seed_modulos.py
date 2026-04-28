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

        # Limpiamos modulos existentes para asegurar la nueva malla
        cursor.execute("DELETE FROM modulos")

        MALLA = [
            # I. NIVEL BÁSICO
            ("1er SEMESTRE - BÁSICO", "Nivel Básico", [
                "Módulo 1: Introducción a la Informática",
                "Módulo 2: Pensamiento Computacional",
                "Módulo 3: Lógica de Programación I",
                "Módulo 4: Algoritmos I",
                "Módulo 5: Módulo Emergente I (IA básica)"
            ]),
            ("2do SEMESTRE - AUXILIAR", "Nivel Básico", [
                "Módulo 1: Lógica de Programación II",
                "Módulo 2: Estructuras de Control",
                "Módulo 3: Funciones",
                "Módulo 4: Bases de Datos Básicas",
                "Módulo 5: Módulo Emergente II (Prompts básicos)"
            ]),
            # II. NIVEL MEDIO
            ("3er SEMESTRE - MEDIO I", "Nivel Medio", [
                "Módulo 1: Programación con Python",
                "Módulo 2: Estructuras de Datos",
                "Módulo 3: Bases de Datos I",
                "Módulo 4: Sistemas Operativos y Redes",
                "Módulo 5: Módulo Emergente III (Prompt estructurado)"
            ]),
            ("4to SEMESTRE - MEDIO II", "Nivel Medio", [
                "Módulo 1: Frontend",
                "Módulo 2: Backend Básico",
                "Módulo 3: Base de Datos II",
                "Módulo 4: Control de Versiones",
                "Módulo 5: Módulo Emergente IV (Contexto IA)"
            ]),
            # III. NIVEL SUPERIOR
            ("5to SEMESTRE - SUPERIOR I", "Nivel Superior", [
                "Módulo 1: Frontend Avanzado",
                "Módulo 2: Backend Avanzado",
                "Módulo 3: Arquitectura de Software",
                "Módulo 4: Seguridad Informática",
                "Módulo 5: Módulo Emergente V (SDD)"
            ]),
            ("6to SEMESTRE - SUPERIOR II", "Nivel Superior", [
                "Módulo 1: DevOps Básico",
                "Módulo 2: Testing de Software",
                "Módulo 3: Despliegue",
                "Módulo 4: Gestión de Proyectos",
                "Módulo 5: Módulo Emergente VI (Flujo con IA)"
            ]),
            # IV. NIVEL INGENIERÍA
            ("7mo SEMESTRE - INGENIERÍA I", "Nivel Ingeniería", [
                "Módulo 1: Estructuras de Datos Avanzadas",
                "Módulo 2: Algoritmos",
                "Módulo 3: Complejidad Computacional",
                "Módulo 4: Bases de Datos Avanzadas",
                "Módulo 5: Módulo Emergente VII (Validación IA)"
            ]),
            ("8vo SEMESTRE - INGENIERÍA II", "Nivel Ingeniería", [
                "Módulo 1: Arquitectura Avanzada",
                "Módulo 2: Cloud Computing",
                "Módulo 3: Infraestructura",
                "Módulo 4: Seguridad Avanzada",
                "Módulo 5: Módulo Emergente VIII (Automatización IA)"
            ]),
            ("9no SEMESTRE - INGENIERÍA III", "Nivel Ingeniería", [
                "Módulo 1: IA en Desarrollo",
                "Módulo 2: Spec-Driven Development (SDD)",
                "Módulo 3: Ingeniería de Prompts",
                "Módulo 4: Automatización Avanzada",
                "Módulo 5: Módulo Emergente IX (Ética IA)"
            ]),
            ("10mo SEMESTRE - INGENIERÍA IV", "Nivel Ingeniería", [
                "Módulo 1: Proyecto de Grado",
                "Módulo 2: Documentación Técnica",
                "Módulo 3: Emprendimiento Tecnológico",
                "Módulo 4: Inserción Laboral",
                "Módulo 5: Módulo Emergente X (IA aplicada)"
            ])
        ]

        # Insertar modulos
        orden_general = 1
        for subnivel, nivel, modulos_nombres in MALLA:
            for m_idx, m_nombre in enumerate(modulos_nombres):
                cursor.execute(
                    "INSERT INTO modulos (nombre, nivel, subnivel, orden) VALUES (%s, %s, %s, %s) RETURNING id",
                    (m_nombre, nivel, subnivel, orden_general)
                )
                m_id = cursor.fetchone()[0]
                orden_general += 1

                # Para cada módulo, creamos 4 temas teóricos (el prompt original pasaba 4 temas por módulo)
                # Aquí simplemente insertamos 4 temas base (se pueden editar luego en el panel)
                for tema_num in range(1, 5):
                    cursor.execute(
                        "INSERT INTO contenidos (modulo_id, tipo, titulo, url, tema_num) VALUES (%s,%s,%s,%s,%s)",
                        (m_id, "teoria", f"Tema {tema_num}", "", tema_num)
                    )
                    # Insertamos también recursos multimedia para tener la estructura "Pro"
                    for tipo_recurso in ["video", "evaluacion"]:
                        cursor.execute(
                            "INSERT INTO contenidos (modulo_id, tipo, titulo, url, tema_num) VALUES (%s,%s,%s,%s,%s)",
                            (m_id, tipo_recurso, f"Recurso {tema_num} - {tipo_recurso.capitalize()}", "", tema_num)
                        )

        connection.commit()
        return orden_general - 1 # Retorna la cantidad de módulos creados
    except Exception as e:
        print(f"Error: {e}")
        return 0

    finally:
        if 'connection' in locals() and connection:
            cursor.close(); connection.close()

if __name__ == "__main__":
    seed_data()
