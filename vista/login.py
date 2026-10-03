"""Ventana de inicio de sesion de la aplicacion."""

import tkinter as tk
from collections.abc import Callable


class LoginView(tk.Tk):
    """Interfaz de login que delega la autenticacion al controlador."""

    def __init__(self, on_login: Callable[[str, str], None] | None = None) -> None:
        super().__init__()
        self.on_login = on_login

        self.title("Iniciar sesion")
        self.geometry("380x380")
        self.resizable(False, False)
        self.configure(bg="#f3f5f7")

        panel = tk.Frame(self, bg="white", padx=32, pady=28)
        panel.pack(expand=True, fill="both", padx=24, pady=24)

        tk.Label(
            panel,
            text="Bienvenido",
            font=("Segoe UI", 20, "bold"),
            bg="white",
            fg="#17212b",
        ).pack(anchor="w")
        tk.Label(
            panel,
            text="Inicia sesion para continuar",
            font=("Segoe UI", 10),
            bg="white",
            fg="#637381",
        ).pack(anchor="w", pady=(2, 20))

        tk.Label(panel, text="Usuario", font=("Segoe UI", 10), bg="white").pack(anchor="w")
        self.username_entry = tk.Entry(panel, font=("Segoe UI", 11), relief="solid", bd=1)
        self.username_entry.pack(fill="x", ipady=6, pady=(5, 14))

        tk.Label(panel, text="Contrasena", font=("Segoe UI", 10), bg="white").pack(anchor="w")
        self.password_entry = tk.Entry(
            panel, font=("Segoe UI", 11), relief="solid", bd=1, show="*"
        )
        self.password_entry.pack(fill="x", ipady=6, pady=(5, 16))
        self.password_entry.bind("<Return>", lambda _event: self.submit())

        self.status_label = tk.Label(
            panel, text="", font=("Segoe UI", 9), bg="white", fg="#b42318"
        )
        self.status_label.pack(anchor="w", pady=(0, 8))

        tk.Button(
            panel,
            text="Iniciar sesion",
            command=self.submit,
            font=("Segoe UI", 10, "bold"),
            bg="#176b5b",
            fg="white",
            activebackground="#125648",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            pady=9,
        ).pack(fill="x")

        self.username_entry.focus_set()

    def submit(self) -> None:
        """Valida los campos y entrega las credenciales al controlador."""
        username = self.username_entry.get().strip()
        password = self.password_entry.get()

        if not username or not password:
            self.status_label.config(text="Completa el usuario y la contrasena.")
            return

        if self.on_login is None:
            self.status_label.config(text="Falta conectar la accion del controlador.")
            return

        self.status_label.config(text="")
        self.on_login(username, password)


if __name__ == "__main__":
    LoginView().mainloop()