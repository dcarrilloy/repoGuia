"""Logica basica de autenticacion para la aplicacion."""

from collections.abc import Mapping

from modelo.usuario import Usuario


class AuthenticationController:
    """Coordina la autenticacion y conserva el usuario de la sesion actual."""

    def __init__(self, users: Mapping[str, Usuario] | None = None) -> None:
        self._users = dict(users) if users is not None else {
            "admin": Usuario(
                nombre_usuario="admin",
                correo="admin@example.com",
                contrasena_hash=Usuario.generar_hash_contrasena("admin123"),
            )
        }
        self._authenticated_user: Usuario | None = None

    @property
    def authenticated_user(self) -> Usuario | None:
        """Usuario autenticado, o None si no hay una sesion valida."""
        return self._authenticated_user

    def authenticate(self, username: str, password: str) -> bool:
        """Valida credenciales y actualiza el usuario de la sesion."""
        user = self._users.get(username)
        if user is not None and user.verificar_contrasena(password):
            self._authenticated_user = user
            return True

        self._authenticated_user = None
        return False