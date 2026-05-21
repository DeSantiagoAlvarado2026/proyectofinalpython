import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
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

    titulo = tk.Label(
        reg,
        text="Registro de Productos",
        font=("Orbitron", 20),
        bg=COLOR_FONDO,
        fg="white"
    )

    titulo.pack(pady=20)

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

    # DESCRIPCIÓN
    crear_label("Descripción").pack(pady=5)

    txt_desc = crear_entry()
    txt_desc.pack(pady=5)

    # PRECIO
    crear_label("Precio").pack(pady=5)

    txt_precio = crear_entry()
    txt_precio.pack(pady=5)

    # CATEGORÍA
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

    ven = tk.Toplevel()
    ven.title("Registro de Ventas")
    ven.geometry("450x520")
    ven.resizable(False, False)
    ven.configure(bg=COLOR_FONDO)

    productos = {}

    try:

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        archivof = os.path.join(BASE_DIR, "productos.txt")

        with open(archivof, "r", encoding="utf-8") as archivo:

            for linea in archivo:

                partes = linea.strip().split("|")

                if len(partes) == 4:

                    idp, desc, precio, cat = partes
                    productos[desc] = float(precio)

    except FileNotFoundError:

        messagebox.showerror(
            "Error",
            "No se encontró el archivo productos.txt"
        )

        ven.destroy()
        return

    lista_productos = list(productos.keys())

    # PRODUCTO
    lbl_prod = tk.Label(
        ven,
        text="Producto:",
        font=("Arial", 12),
        bg=COLOR_FONDO,
        fg="white"
    )

    lbl_prod.pack(pady=5)

    cb_producto = ttk.Combobox(
        ven,
        values=lista_productos,
        font=("Arial", 12),
        state="readonly"
    )

    cb_producto.pack(pady=5)

    # PRECIO
    lbl_precio = tk.Label(
        ven,
        text="Precio Unitario:",
        font=("Arial", 12),
        bg=COLOR_FONDO,
        fg="white"
    )

    lbl_precio.pack(pady=5)

    txt_precio = tk.Entry(
        ven,
        font=("Arial", 12)
    )

    txt_precio.pack(pady=5)

    # CANTIDAD
    lbl_cantidad = tk.Label(
        ven,
        text="Cantidad:",
        font=("Arial", 12),
        bg=COLOR_FONDO,
        fg="white"
    )

    lbl_cantidad.pack(pady=5)

    txt_cantidad = tk.Entry(
        ven,
        font=("Arial", 12)
    )

    txt_cantidad.pack(pady=5)

    # TOTAL
    lbl_total = tk.Label(
        ven,
        text="TOTAL FINAL:",
        font=("Arial", 14, "bold"),
        bg=COLOR_FONDO,
        fg="yellow"
    )

    lbl_total.pack(pady=10)

    txt_total = tk.Entry(
        ven,
        font=("Arial", 14, "bold"),
        justify="center"
    )

    txt_total.pack(pady=5)

    # ------------------------------------
    # CALCULAR TOTAL
    # ------------------------------------
    def calcular_total():

        try:

            precio = float(txt_precio.get())
            cantidad = float(txt_cantidad.get())

            total = precio * cantidad

            txt_total.delete(0, tk.END)
            txt_total.insert(0, f"{total:.2f}")

        except:

            messagebox.showerror(
                "Error",
                "Ingresa valores numéricos válidos"
            )

    # ------------------------------------
    # ACTUALIZAR PRECIO
    # ------------------------------------
    def actualizar_precio(event):

        prod = cb_producto.get()

        if prod in productos:

            txt_precio.delete(0, tk.END)
            txt_precio.insert(0, productos[prod])

    # ------------------------------------
    # REGISTRAR VENTA
    # ------------------------------------
    def registrar_venta():

        prod = cb_producto.get()
        precio = txt_precio.get()
        cantidad = txt_cantidad.get()
        total = txt_total.get()

        if prod == "" or precio == "" or cantidad == "" or total == "":

            messagebox.showwarning(
                "Campos Vacíos",
                "Todos los campos deben estar completos."
            )

            return

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        archivov = os.path.join(BASE_DIR, "ventas.txt")

        with open(archivov, "a", encoding="utf-8") as archivo:

            archivo.write(
                f"{prod}|{precio}|{cantidad}|{total}\n"
            )

        messagebox.showinfo(
            "Venta Registrada",
            "La venta se registró correctamente."
        )

        cb_producto.set("")
        txt_precio.delete(0, tk.END)
        txt_cantidad.delete(0, tk.END)
        txt_total.delete(0, tk.END)

    # EVENTOS
    cb_producto.bind(
        "<<ComboboxSelected>>",
        actualizar_precio
    )

    # BOTÓN CALCULAR
    btn_calcular = tk.Button(
        ven,
        text="Calcular Total",
        command=calcular_total,
        font=("Orbitron", 12),
        bg="#00b894",
        fg="white",
        width=20,
        height=2
    )

    btn_calcular.pack(pady=15)

    # BOTÓN REGISTRAR
    btn_guardar = tk.Button(
        ven,
        text="Registrar Venta",
        command=registrar_venta,
        font=("Orbitron", 12),
        bg=COLOR_NORMAL,
        fg="white",
        width=20,
        height=2
    )

    btn_guardar.pack(pady=10)

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

# LOGO
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

# TITULO
titulo_principal = tk.Label(
    ventana,
    text="Sistema Punto de Venta",
    font=("Orbitron", 20),
    bg=COLOR_FONDO,
    fg="white"
)

titulo_principal.pack(pady=10)

# CREAR BOTONES
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

# BOTONES
btn_reg_prod = crear_boton(
    "Registro de Productos",
    abrir_registro_productos
)

btn_reg_prod.pack(pady=15)

btn_reg_ventas = crear_boton(
    "Registro de Ventas",
    abrir_registro_ventas
)

btn_reg_ventas.pack(pady=15)

btn_reportes = crear_boton(
    "Reportes",
    abrir_reportes
)

btn_reportes.pack(pady=15)

btn_acerca = crear_boton(
    "Acerca de",
    abrir_acerca_de
)

btn_acerca.pack(pady=15)

# EJECUTAR
ventana.mainloop()