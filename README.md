# Aplicacion de login MVC

Aplicacion de escritorio sencilla en Python que integra una ventana de inicio de sesion con un modelo de usuario y un controlador de autenticacion.

## Requisitos

- Python 3.10 o posterior.
- Tkinter, incluido normalmente con la instalacion de Python.
- No requiere paquetes externos.

## Ejecucion

Desde la carpeta raiz del proyecto, ejecuta:

```powershell
python main.py
```

Credenciales de demostracion:

- Usuario: `admin`
- Contrasena: `admin123`

La ventana informa si el inicio de sesion fue correcto. La interfaz puede ejecutarse desde el punto de entrada `main.py`.

## Estructura

- `modelo/usuario.py`: representa un usuario y genera/verifica hashes de contrasena con PBKDF2-HMAC-SHA256 y sal aleatoria.
- `controlador/autenticacion.py`: valida las credenciales usando el modelo y mantiene el usuario autenticado en memoria.
- `vista/login.py`: presenta el formulario y muestra el resultado de autenticacion.
- `main.py`: conecta modelo/controlador con la vista y arranca la aplicacion.

## Alcance

Es una demostracion local: el usuario de ejemplo se crea al iniciar la aplicacion, no hay base de datos, registro ni persistencia de sesiones. Para un despliegue real, las cuentas deben almacenarse en un sistema persistente y la configuracion debe gestionarse fuera del codigo.