import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# -------------------------
# COLORES
# -------------------------
COLOR_FONDO = "#1e1e2f"
COLOR_NORMAL = "#7b2cbf"
COLOR_HOVER = "#9d4edd"

# -------------------------
# EFECTO HOVER
# -------------------------
def efecto_hover(boton):
    boton.bind("<Enter>", lambda e: boton.config(bg=COLOR_HOVER))
    boton.bind("<Leave>", lambda e: boton.config(bg=COLOR_NORMAL))

# -------------------------
# REGISTRO DE PRODUCTOS
# -------------------------
def abrir_registro_productos():

    reg = tk.Toplevel()
    reg.title("Registro de Productos")
    reg.geometry("500x550")
    reg.resizable(False, False)
    reg.configure(bg=COLOR_FONDO)

    # TITULO
    titulo = tk.Label(
        reg,
        text="Registro de Productos",
        font=("Orbitron", 20),
        bg=COLOR_FONDO,
        fg="white"
    )
    titulo.pack(pady=20)

    # FUNCIONES CAMPOS
    def crear_label(texto):
        return tk.Label(
            reg,
            text=texto,
            font=("Arial", 12),
            bg=COLOR_FONDO,
            fg="white"
        )

    def crear_entry():
        return tk.Entry(
            reg,
            font=("Arial", 12),
            width=30
        )

    # ID
    crear_label("ID del Producto").pack(pady=5)
    txt_id = crear_entry()
    txt_id.pack(pady=5)

    # DESCRIPCION
    crear_label("Descripción").pack(pady=5)
    txt_desc = crear_entry()
    txt_desc.pack(pady=5)

    # PRECIO
    crear_label("Precio").pack(pady=5)
    txt_precio = crear_entry()
    txt_precio.pack(pady=5)

    # CATEGORIA
    crear_label("Categoría").pack(pady=5)
    txt_categoria = crear_entry()
    txt_categoria.pack(pady=5)

    # GUARDAR PRODUCTO
    def guardar_producto():

        id_prod = txt_id.get().strip()
        descripcion = txt_desc.get().strip()
        precio = txt_precio.get().strip()
        categoria = txt_categoria.get().strip()

        if id_prod == "" or descripcion == "" or precio == "" or categoria == "":
            messagebox.showwarning(
                "Campos Vacíos",
                "Complete todos los campos"
            )
            return

        try:
            float(precio)
        except:
            messagebox.showerror(
                "Error",
                "El precio debe ser numérico"
            )
            return

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        archivo = os.path.join(BASE_DIR, "productos.txt")

        with open(archivo, "a", encoding="utf-8") as archivo:
            archivo.write(
                f"{id_prod}|{descripcion}|{precio}|{categoria}\n"
            )

        messagebox.showinfo(
            "Guardado",
            "Producto guardado correctamente"
        )

        txt_id.delete(0, tk.END)
        txt_desc.delete(0, tk.END)
        txt_precio.delete(0, tk.END)
        txt_categoria.delete(0, tk.END)

    # BOTON
    btn_guardar = tk.Button(
        reg,
        text="Guardar Producto",
        command=guardar_producto,
        font=("Orbitron", 12),
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

    efecto_hover(btn_guardar)
    btn_guardar.pack(pady=30)

# -------------------------
# REGISTRO DE VENTAS
# -------------------------
def abrir_registro_ventas():
    messagebox.showinfo(
        "Registro de Ventas",
        "Aquí irá el módulo de ventas"
    )

# -------------------------
# REPORTES
# -------------------------
def abrir_reportes():
    messagebox.showinfo(
        "Reportes",
        "Aquí irá el módulo de reportes"
    )

# -------------------------
# ACERCA DE
# -------------------------
def abrir_acerca_de():
    messagebox.showinfo(
        "Acerca de",
        "Punto de Venta de Ropa\nProyecto Escolar\nVersión 1.0"
    )

# -------------------------
# VENTANA PRINCIPAL
# -------------------------
ventana = tk.Tk()
ventana.title("Punto de Venta - DebyAlex")
ventana.geometry("500x700")
ventana.resizable(False, False)
ventana.configure(bg=COLOR_FONDO)

# -------------------------
# LOGO
# -------------------------
try:

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    imagen = Image.open(
        os.path.join(BASE_DIR, "logo.png")
    )

    imagen = imagen.resize((250, 250))

    img_logo = ImageTk.PhotoImage(imagen)

    lbl_logo = tk.Label(
        ventana,
        image=img_logo,
        bg=COLOR_FONDO
    )

    lbl_logo.pack(pady=20)

except:

    lbl_logo = tk.Label(
        ventana,
        text="(Aquí va el logo)",
        font=("Arial", 16),
        bg=COLOR_FONDO,
        fg="white"
    )

    lbl_logo.pack(pady=40)

# -------------------------
# TITULO
# -------------------------
titulo_principal = tk.Label(
    ventana,
    text="Sistema Punto de Venta",
    font=("Orbitron", 20),
    bg=COLOR_FONDO,
    fg="white"
)

titulo_principal.pack(pady=10)

# -------------------------
# CREAR BOTONES
# -------------------------
def crear_boton(texto, comando):

    btn = tk.Button(
        ventana,
        text=texto,
        command=comando,
        font=("Orbitron", 12),
        bg=COLOR_NORMAL,
        fg="white",
        activebackground=COLOR_HOVER,
        activeforeground="white",
        width=22,
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
btn_reg_prod = crear_boton(
    "Registro de Productos",
    abrir_registro_productos
)

btn_reg_prod.pack(pady=10)

btn_reg_ventas = crear_boton(
    "Registro de Ventas",
    abrir_registro_ventas
)

btn_reg_ventas.pack(pady=10)

btn_reportes = crear_boton(
    "Reportes",
    abrir_reportes
)

btn_reportes.pack(pady=10)

btn_acerca = crear_boton(
    "Acerca de",
    abrir_acerca_de
)

btn_acerca.pack(pady=10)

# -------------------------
# INICIO
# -------------------------
ventana.mainloop()