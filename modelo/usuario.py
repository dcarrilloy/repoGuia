"""Modelo basico de usuario."""

import hashlib
import hmac
import secrets
from dataclasses import dataclass


@dataclass
class Usuario:
    """Datos principales de un usuario de la aplicacion."""

    nombre_usuario: str
    correo: str
    contrasena_hash: str

    @staticmethod
    def generar_hash_contrasena(contrasena: str) -> str:
        """Genera un hash PBKDF2 con una sal aleatoria."""
        salt = secrets.token_bytes(16)
        password_hash = hashlib.pbkdf2_hmac(
            "sha256", contrasena.encode("utf-8"), salt, 310_000
        )
        return f"pbkdf2_sha256${salt.hex()}${password_hash.hex()}"

    def verificar_contrasena(self, contrasena: str) -> bool:
        """Verifica una contrasena contra el hash almacenado."""
        try:
            algorithm, salt_hex, expected_hash = self.contrasena_hash.split("$", 2)
            if algorithm != "pbkdf2_sha256":
                return False
            salt = bytes.fromhex(salt_hex)
        except ValueError:
            return False

        password_hash = hashlib.pbkdf2_hmac(
            "sha256", contrasena.encode("utf-8"), salt, 310_000
        ).hex()
        return hmac.compare_digest(password_hash, expected_hash)