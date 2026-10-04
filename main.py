"""Punto de entrada de la aplicacion."""

from controlador.autenticacion import AuthenticationController
from vista.login import LoginView


def main() -> None:
    """Construye y ejecuta la interfaz conectada al controlador."""
    controller = AuthenticationController()
    view = LoginView(on_login=controller.authenticate)
    view.mainloop()


if __name__ == "__main__":
    main()