# Proyecto Final Django — Blog + Mensajería + Perfil de Usuario

## 📌 Descripción

Este proyecto fue desarrollado con Django como entrega final.

Video Demo de la app: https://drive.google.com/file/d/1-Tu1r0219FZb42PKvvZiqYhMF7uGkbhv/view?usp=sharing


La aplicación permite:

* Crear y administrar páginas tipo blog.
* Registro y autenticación de usuarios.
* Perfil de usuario editable.
* Subida de avatar e información personal.
* Sistema de mensajería entre usuarios.
* Editor de texto enriquecido mediante CKEditor.

---

# 🚀 Funcionalidades

## 👤 Sistema de Usuarios

* Registro de usuario.
* Login.
* Logout.
* Perfil de usuario.
* Edición de perfil.
* Avatar personalizado.
* Bio personalizada.

---

## 📄 CRUD de Páginas

Los usuarios pueden:

* Crear páginas.
* Ver listado de páginas.
* Ver detalle de una página.
* Editar páginas.
* Eliminar páginas.

Cada página contiene:

* Título
* Subtítulo
* Contenido enriquecido con CKEditor
* Imagen
* Fecha de creación

---

## 💬 Sistema de Mensajería

Los usuarios autenticados pueden:

* Enviar mensajes.
* Ver bandeja de entrada.
* Ver mensajes enviados.
* Abrir detalle del mensaje.

---

# 🛠️ Tecnologías Utilizadas

* Python 3.13
* Django 6
* SQLite3
* CKEditor
* Pillow
* HTML
* CSS

---

# 📂 Estructura del Proyecto

```text
mi_proyecto/
│
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│
├── app/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│
├── media/
├── manage.py
└── requirements.txt
La mensajería fue implementada dentro de la app principal mediante el modelo Mensaje y vistas específicas para inbox, enviados y detalle.
```

---

# ⚙️ Instalación

## 1️⃣ Clonar repositorio

```bash
git clone https://github.com/Nahircufre/Entrega-Final---Cufre-Nahir
```

---

## 2️⃣ Crear entorno virtual

```bash
python -m venv venv
```

---

## 3️⃣ Activar entorno virtual

### Windows

```bash
venv\Scripts\activate
```

---

## 4️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Aplicar migraciones

```bash
python manage.py migrate
```

---

## 6️⃣ Ejecutar servidor

```bash
python manage.py runserver
```

---

# 🔐 Usuario Admin

Para crear un administrador:

```bash
python manage.py createsuperuser
```

Luego acceder a:

```text
http://127.0.0.1:8000/admin/
```

---



# ✍️ Autor

**Nahir Cufré**

Proyecto desarrollado como entrega final  para Python utilizando Django.
Para Coderhouse

---

# ✅ Estado del Proyecto

Proyecto funcional con:

* Autenticación
* CRUD
* Perfil con avatar
* Mensajería
* Editor enriquecido
* Manejo de archivos multimedia

