# Django-Coderhouse

Este es un proyecto Django desarrollado en el curso de Coderhouse. Contiene una aplicación llamada **BlogApp**, que maneja blogs con formularios y plantillas.

## 💁️ Estructura del Proyecto

```
Choquehuanca-PythonProject-coderhouse/
│── djangoproject/          # Configuración principal de Django
│   ├─ settings.py         # Configuración general del proyecto
│   ├─ urls.py             # Rutas del proyecto
│   ├─ wsgi.py / asgi.py   # Archivos de despliegue
│
│── home/                   # Aplicación principal del proyecto
│   ├─ migrations/         # Migraciones de la base de datos
│   ├─ templates/home/     # Plantillas HTML
│   ├─ static/             # Archivos estáticos (CSS, JS, imágenes)
│   ├─ admin.py            # Configuración del panel de administración
│   ├─ apps.py             # Configuración de la aplicación
│   ├─ forms.py            # Formularios Django
│   ├─ models.py           # Modelos de base de datos
│   ├─ tests.py            # Pruebas unitarias
│   ├─ urls.py             # Rutas específicas de la app
│   └─ views.py            # Vistas de la aplicación
│
│── templates/              # Plantillas HTML globales
│── db.sqlite3              # Base de datos SQLite
│── manage.py               # Archivo para ejecutar comandos Django
│── requirements.txt        # Dependencias del proyecto
│── readme.md               # Este archivo
```

## 🚀 Instalación y Configuración

### 1️⃣ Clonar el repositorio
```sh
git clone <URL_DEL_REPOSITORIO>
cd Choquehuanca-PythonProject-coderhouse
```

### 2️⃣ Crear y activar un entorno virtual
```sh
python -m venv env
source env/bin/activate  # Mac/Linux
env\Scripts\activate     # Windows
```

### 3️⃣ Instalar dependencias
```sh
pip install -r requirements.txt
```

### 4️⃣ Ejecutar el servidor
```sh
python manage.py runserver
```

### 5️⃣ Ejecuta las migraciones de la base de datos:
```sh
	python manage.py makemigrations
	python manage.py migrate 

```
---

## 📌 Funcionalidades del Proyecto

✅ **Manejo de Blogs:** Creación, edición y eliminación de blogs.  
✅ **Formularios con Django Forms.**  
✅ **Uso de plantillas en `templates/home/`.**  
✅ **Base de datos en SQLite3.**  
✅ **Bootstrap para diseño responsivo.**  


---

🔹 **¡Gracias por visitar este proyecto!** 🚀

