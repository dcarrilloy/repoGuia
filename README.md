# Estructura MVC

Base vacia para organizar una aplicacion Python con el patron Modelo-Vista-Controlador.

- `modelo/`: datos y reglas de negocio.
- `vista/`: presentacion y entrada/salida.
- `controlador/`: coordina el modelo y la vista.

Cada carpeta contiene un `__init__.py` con una breve descripcion para marcarla como paquete Python. Al crecer el proyecto, se pueden agregar modulos dentro de cada paquete y, si resulta conveniente, exportar sus clases desde `__init__.py`.