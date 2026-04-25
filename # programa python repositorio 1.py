# programa python en repositorio 
import tkinter as tk 
from tkinter import font

ventana = tk.Tk()
ventana.title("Programa para subir a Repositorio")
ventana.geometry("350x330")
ventana.configure(bg="black")  # Fondo negro

# Intentar usar una fuente gótica (si no existe, usa una alternativa)
try:
    fuente_gotica = font.Font(family="Old English Text MT", size=40, weight="bold")
except:
    fuente_gotica = font.Font(family="Times New Roman", size=40, weight="bold")

# Etiqueta con estilo mejorado
etiqueta = tk.Label(
    ventana, 
    text="Este programa es de Debora y Alexander",
    font=fuente_gotica,
    fg="#800080",   # Morado
    bg="black"
)

etiqueta.pack(pady=40)

ventana.mainloop()