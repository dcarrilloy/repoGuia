"""Pruebas unitarias del controlador de autenticacion."""

import unittest

from controlador.autenticacion import AuthenticationController
from modelo.usuario import Usuario


class AuthenticationControllerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.user = Usuario(
            nombre_usuario="ana",
            correo="ana@example.com",
            contrasena_hash=Usuario.generar_hash_contrasena("secreto-123"),
        )
        self.controller = AuthenticationController({"ana": self.user})

    def test_autentica_usuario_y_guarda_sesion(self) -> None:
        self.assertTrue(self.controller.authenticate("ana", "secreto-123"))
        self.assertIs(self.controller.authenticated_user, self.user)

    def test_contrasena_incorrecta_no_autentica(self) -> None:
        self.assertFalse(self.controller.authenticate("ana", "incorrecta"))
        self.assertIsNone(self.controller.authenticated_user)

    def test_usuario_desconocido_no_autentica(self) -> None:
        self.assertFalse(self.controller.authenticate("desconocido", "secreto-123"))
        self.assertIsNone(self.controller.authenticated_user)

    def test_fallo_de_autenticacion_limpia_sesion_anterior(self) -> None:
        self.controller.authenticate("ana", "secreto-123")

        self.assertFalse(self.controller.authenticate("ana", "incorrecta"))
        self.assertIsNone(self.controller.authenticated_user)


if __name__ == "__main__":
    unittest.main()