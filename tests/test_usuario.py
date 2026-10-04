"""Pruebas unitarias del modelo de usuario."""

import unittest

from modelo.usuario import Usuario


class UsuarioTests(unittest.TestCase):
    def test_hash_verifica_contrasena_y_usa_sal_aleatoria(self) -> None:
        password = "secreto-123"
        first_hash = Usuario.generar_hash_contrasena(password)
        second_hash = Usuario.generar_hash_contrasena(password)
        user = Usuario("ana", "ana@example.com", first_hash)

        self.assertNotEqual(first_hash, second_hash)
        self.assertTrue(user.verificar_contrasena(password))
        self.assertFalse(user.verificar_contrasena("otra-contrasena"))

    def test_hash_malformado_no_verifica(self) -> None:
        user = Usuario("ana", "ana@example.com", "hash-invalido")

        self.assertFalse(user.verificar_contrasena("secreto-123"))


if __name__ == "__main__":
    unittest.main()