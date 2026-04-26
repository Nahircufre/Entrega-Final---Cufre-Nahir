Mi Primera Página - Nahir Cufré

App: Blog con Django

Este proyecto es una aplicación web desarrollada con Django que permite crear y administrar páginas tipo blog, con sistema de autenticación, perfiles y navegación completa.

--------------------------------------------------

FUNCIONALIDADES PRINCIPALES

🏠 Página de inicio
Ruta: /

- Página principal del sitio
- Navegación hacia todas las secciones
- Diseño base reutilizable

--------------------------------------------------

👩 Acerca de mí
Ruta: /about/

- Vista informativa sobre el dueño del sitio
- Acceso visible desde la barra de navegación

--------------------------------------------------

📚 Pages / Blog
Ruta: /pages/

Permite:

- Visualizar todas las páginas creadas
- Mostrar título y subtítulo
- Acceder al detalle mediante “Leer más”
- Mostrar mensaje si no existen páginas

--------------------------------------------------

📝 Crear página
Ruta: /pages/create/

Permite:

- Crear una nueva página del blog
- Agregar título
- Agregar subtítulo
- Escribir contenido enriquecido con CKEditor
- Subir imagen
- Guardar fecha automáticamente

--------------------------------------------------

🔎 Detalle de página
Ruta: /pages/<id>/

Permite:

- Ver contenido completo
- Mostrar imagen
- Visualizar fecha de creación
- Acceder a editar o eliminar

--------------------------------------------------

✏️ Editar página
Ruta: /pages/<id>/edit/

- Solo disponible para usuarios logueados
- Permite modificar contenido existente

--------------------------------------------------

🗑️ Eliminar página
Ruta: /pages/<id>/delete/

- Solo disponible para usuarios logueados
- Confirmación antes de eliminar

--------------------------------------------------

🔐 Sistema de usuarios

Registro
Ruta: /accounts/signup/

Permite:

- Crear usuario
- Login automático luego del registro

--------------------------------------------------

Login
Ruta: /accounts/login/

Permite:

- Iniciar sesión

--------------------------------------------------

Logout
Ruta: /accounts/logout/

Permite:

- Cerrar sesión

--------------------------------------------------

Perfil
Ruta: /accounts/profile/

Permite:

- Visualizar usuario logueado
- Ver email y datos básicos

--------------------------------------------------

🎨 Interfaz

- Navbar superior
- Template base reutilizable
- Diseño simple y limpio
- Templates heredados
- Navegación visible entre secciones

--------------------------------------------------

⚙️ Tecnologías utilizadas

- Python
- Django
- HTML
- CSS básico
- SQLite
- Django CKEditor
- Pillow

--------------------------------------------------

📂 Estructura principal

mi_proyecto/
│
├── app/
├── accounts/
├── templates/
├── media/
├── static/
└── db.sqlite3

--------------------------------------------------

▶️ Orden para probar la aplicación

1. Ejecutar servidor:

python manage.py runserver

2. Ingresar a:

http://127.0.0.1:8000/

--------------------------------------------------

🌐 Rutas principales

Inicio
/

About
/about/

Pages
/pages/

Crear página
/pages/create/

Login
/accounts/login/

Signup
/accounts/signup/

Perfil
/accounts/profile/

Logout
/accounts/logout/

Admin Django
/admin/

--------------------------------------------------

✅ Funcionalidades implementadas

- Home
- About
- CRUD completo de páginas
- Login
- Logout
- Signup
- Perfil
- Upload de imágenes
- CKEditor
- Navbar
- Herencia de templates
- CBV (Class Based Views)
- LoginRequiredMixin
- Decorators
- Panel Admin
- Mensajes de confirmación