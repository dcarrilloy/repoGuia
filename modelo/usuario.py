"""Modelo basico de usuario."""

from dataclasses import dataclass


@dataclass
class Usuario:
    """Datos principales de un usuario de la aplicacion."""

    nombre_usuario: str
    correo: str
    contrasena_hash: str