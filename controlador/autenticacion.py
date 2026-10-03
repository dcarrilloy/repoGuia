"""Logica basica de autenticacion para la aplicacion."""

import hmac
from collections.abc import Mapping


class AuthenticationController:
    """Valida credenciales contra un conjunto de usuarios configurado."""

    def __init__(self, users: Mapping[str, str] | None = None) -> None:
        self._users = users if users is not None else {"admin": "admin123"}

    def authenticate(self, username: str, password: str) -> bool:
        """Devuelve si el usuario y la contrasena coinciden."""
        expected_password = self._users.get(username)
        return expected_password is not None and hmac.compare_digest(
            expected_password.encode("utf-8"), password.encode("utf-8")
        )