import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# -------------------------
# FUNCIONES
# -------------------------
def abrir_registro_productos():
    messagebox.showinfo("Registro de Productos", "Aquí irá el módulo de registro de productos.")

def abrir_registro_ventas():
    messagebox.showinfo("Registro de Ventas", "Aquí irá el módulo de registro de ventas.")

def abrir_reportes():
    messagebox.showinfo("Reportes", "Aquí irá el módulo de reportes.")

def abrir_acerca_de():
    messagebox.showinfo("Acerca de", "Punto de Venta de Ropa\n Proyecto Escolar\n Versión 1.0")


# -------------------------
# VENTANA PRINCIPAL
# -------------------------
ventana = tk.Tk()
ventana.title("Punto de Venta - DebyAlex")
ventana.geometry("500x600")
ventana.resizable(False, False)
ventana.configure(bg="#1e1e2f")  # Fondo oscuro gamer


# -------------------------
# LOGO
# -------------------------
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    imagen = Image.open(os.path.join(BASE_DIR, "logo.png"))
    imagen = imagen.resize((250, 250))
    img_logo = ImageTk.PhotoImage(imagen)

    lbl_logo = tk.Label(ventana, image=img_logo, bg="#1e1e2f")
    lbl_logo.pack(pady=20)
except:
    lbl_sin_logo = tk.Label(
        ventana,
        text="(Aquí va el logo del sistema)",
        font=("Arial", 14),
        bg="#1e1e2f",
        fg="white"
    )
    lbl_sin_logo.pack(pady=40)


# -------------------------
# ESTILO BOTONES
# -------------------------
COLOR_NORMAL = "#7b2cbf"   # violeta
COLOR_HOVER = "#9d4edd"    # violeta claro

def efecto_hover(boton):
    boton.bind("<Enter>", lambda e: boton.config(bg=COLOR_HOVER))
    boton.bind("<Leave>", lambda e: boton.config(bg=COLOR_NORMAL))


def crear_boton(texto, comando):
    btn = tk.Button(
        ventana,
        text=texto,
        command=comando,
        font=("Orbitron", 12),  # si no tienes Orbitron usa Arial
        bg=COLOR_NORMAL,
        fg="white",
        activebackground=COLOR_HOVER,
        activeforeground="white",
        width=20,
        height=2,
        bd=4,
        relief="raised",
        cursor="hand2"
    )
    efecto_hover(btn)
    return btn


# -------------------------
# BOTONES
# -------------------------
btn_reg_prod = crear_boton("Registro de Productos", abrir_registro_productos)
btn_reg_prod.pack(pady=10)

btn_reg_ventas = crear_boton("Registro de Ventas", abrir_registro_ventas)
btn_reg_ventas.pack(pady=10)

btn_reportes = crear_boton("Reportes", abrir_reportes)
btn_reportes.pack(pady=10)

btn_acerca = crear_boton("Acerca de", abrir_acerca_de)
btn_acerca.pack(pady=10)


# -------------------------
# INICIO
# -------------------------
ventana.mainloop()
