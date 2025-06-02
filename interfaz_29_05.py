import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
import customtkinter as ctk
import threading
import time
from PIL import Image, ImageTk 
import os 
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from scipy.interpolate import interp1d
from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt

#TTK Boostrap
root = ttk.Window(themename = 'lumen')
#Tkinter
#root = tk.Tk()
root.title("Lectura de Peso")
root.geometry("1200x600")
root.protocol("WM_DELETE_WINDOW", on_close)

#panel1
panelLateral = SlidePanel(root,0,0.3)

#panelIzqAbajo = ttk.Frame(root,relief='solid')
#panelIzqAbajo.place(x=0, rely=0.5, relwidth= 0.3, relheight=1)

panellateralDown = PanelLateralDown(root, 0, 0.3)

notebook = NotebookFrame(root)

# Botones de control
#frame_buttons = ctk.CTkFrame(root)
#ttk.Frame(root)
#frame_buttons.pack(pady=10)

# Título de la interfaz
title_label = ttk.Label(panellateralDown, text="Sistema de Balanza", font=("Arial", 24))
title_label.pack(pady=10)

# Etiqueta para mostrar el peso
weight_label = ttk.Label(panellateralDown, text="Peso: --", font=("Arial", 18))
weight_label.pack(pady=20)

start_button = ttk.Button(panellateralDown, text="Iniciar", width=10, command=start_reading, bootstyle='SUCCESS')
start_button.pack(side=ttk.LEFT, padx = 5)#grid(row=0, column=0, padx=10)

stop_button = ttk.Button(panellateralDown, text="Detener", width=10, command=stop_reading,bootstyle='DANGER')
stop_button.pack(side=ttk.RIGHT, padx = 5)#grid(row=0, column=1, padx=10)

reset_button = ttk.Button(panellateralDown, text="Reiniciar", width=10, command=reset_scale,bootstyle='PRIMARY')
reset_button.pack(side=ttk.BOTTOM, pady = 20)#grid(row=1, column=0, columnspan=2, pady=10)

ingresar_button = ttk.Button(panellateralDown, text="Ingresar Cafe", width=10, command=ingreso_cafe,bootstyle='SUCCESS')
ingresar_button.pack(side=ttk.BOTTOM, pady = 20)#grid(row=1, column=0, columnspan=2, pady=10)


# ComboBox para seleccionar imágenes
combo_box = ttk.Combobox(panelLateral, state = "readonly", values=list(rutas_imagenes.keys()))#textvariable=seleccion_tueste)
combo_box.set("Selecciona una imagen")
combo_box.pack(pady=20)
combo_box.bind('<<ComboboxSelected>>', cambiar_imagen)

label_imagen = ttk.Label(panelLateral, text="", anchor="center")  # Asegúrate de usar un label sin texto por defecto
label_imagen.pack(pady=20)
#ttk.Label(panelIzqAbajo, background='yellow').pack(expand=True,fill="both")

# Iniciar la aplicación
root.mainloop()
