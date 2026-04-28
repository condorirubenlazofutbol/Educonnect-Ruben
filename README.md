# 🎓 EduConnect Ruben – Plataforma Educativa Pro & Escalable

> Sistema LMS (Learning Management System) de alto rendimiento, diseñado para la escalabilidad académica. Incluye roles de Administrador, Profesor y Estudiante con una arquitectura moderna PWA.

---

## 🌐 URLs de Producción

| Recurso | URL |
|---|---|
| **Plataforma Web** | [https://condorirubenlazofutbol.github.io/Educonnect-Ruben/](https://condorirubenlazofutbol.github.io/Educonnect-Ruben/) |
| **Página de Acceso** | [https://condorirubenlazofutbol.github.io/Educonnect-Ruben/login.html](https://condorirubenlazofutbol.github.io/Educonnect-Ruben/login.html) |
| **Backend API** | [https://educonnect-backend-production-1d08.up.railway.app](https://educonnect-backend-production-1d08.up.railway.app) |
| **Documentación API** | [/docs](https://educonnect-backend-production-1d08.up.railway.app/docs) |

---

## 🚀 Características de Escalabilidad y Potencia

### 📱 PWA (Progressive Web App)
La plataforma es **instalable** en dispositivos Android, iOS y Windows/Mac. Funciona como una aplicación nativa, con icono en el escritorio y carga optimizada, garantizando acceso rápido para los estudiantes desde cualquier lugar.

### 🛡️ Administración Avanzada y Control Total
Diseñado para gestionar grandes volúmenes de usuarios:
- **Buscador Inteligente:** Filtra miles de alumnos por **Número de Carnet** o Nombre en milisegundos.
- **Control de Pagos (Pausar/Reanudar):** Suspensión inmediata del acceso para alumnos en mora sin borrar sus datos ni progreso.
- **Gestión Masiva:** Carga de semestres completos mediante archivos Excel (.xlsx).
- **Seguridad Pro:** Reseteo de contraseñas por carnet y cambio de credenciales de administrador integrado.

### 👨‍🏫 Gestión de Contenidos Dinámicos
- **Malla Curricular Robusta:** Estructura escalable de 10 Semestres (Básico hasta Ingeniería).
- **Materiales Ilimitados:** Los profesores pueden añadir materiales extra dinámicos (PDF, Video, PPT, Audio) más allá de la malla base.

### 🌐 Optimización SEO y Social Media
Configurado con **Open Graph**, permitiendo que al compartir el enlace en WhatsApp o redes sociales, aparezca la marca oficial y una vista previa profesional.

---

## 🏗️ Arquitectura Técnica

```
Educonnect-Ruben/
├── backend/                  # FastAPI (Python 3.11) + PostgreSQL
│   ├── main.py               # Migraciones automáticas y Startup
│   ├── database.py           # Gestión de Pool de conexiones
│   └── routes/               # Lógica de negocio modularizada
├── frontend/                 # Frontend ligero (Vanilla JS / HTML5 / CSS3)
│   ├── instalar/             # Recursos PWA (Service Worker, Manifest, Iconos)
│   ├── admin/                # Panel de Control Administrativo
│   ├── profesor/             # Gestión de Módulos y Materiales
│   └── student/              # Interfaz de Aprendizaje
└── requirements.txt
```

---

## 👥 Roles del Sistema

| Rol | Capacidades |
|---|---|
| **Administrador** | Control total de usuarios, reportes académicos, carga masiva, búsqueda por CI y suspensión de acceso. |
| **Profesor** | Gestión de sus módulos asignados, publicación de materiales extra y seguimiento de temas. |
| **Estudiante** | Acceso a contenidos por niveles, navegación por pestañas de semestres y consumo de materiales. |

---

## 📐 Capacidad de la Malla
- **10 Semestres** (Básico, Auxiliar, Medio, Superior, Ingeniería).
- **5 Módulos** estándar por semestre.
- **4 Temas** estructurados por módulo (Optimizados para UX).
- **Tipos de material:** Teoría (PDF), PPT, Video, Audio y Evaluación.

---

## 🚀 Stack Tecnológico

| Capa | Tecnología | Razón de uso |
|---|---|---|
| **Backend** | FastAPI | Velocidad asíncrona y escalabilidad horizontal. |
| **Base de Datos** | PostgreSQL | Robustez relacional y seguridad de datos. |
| **Frontend** | Vanilla JS | Carga instantánea sin dependencias pesadas. |
| **Infraestructura** | Railway | Despliegue continuo (CI/CD) automático. |
| **Seguridad** | JWT + bcrypt | Estándar de la industria para sesiones seguras. |

---

## 👨‍💻 Equipo y Desarrollo

- **Líder de Proyecto:** Ruben Lazo
- **Soporte de Ingeniería:** Antigravity AI (Google DeepMind)

---
*EduConnect Ruben v20.0 – "Educación sin límites, tecnología sin fronteras"*
