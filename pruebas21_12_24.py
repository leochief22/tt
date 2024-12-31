import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
import customtkinter as ctk
import threading
import time
from PIL import Image, ImageTk 
import os 
"""import RPi.GPIO as GPIO
from hx711 import HX711  # Asegúrate de tener instalada esta librería

# Configuración de GPIO y la balanza
GPIO.setmode(GPIO.BCM)
hx = HX711(dout_pin=2, pd_sck_pin=3)
hx.zero()"""

# Variable para controlar el bucle de lectura
running = False

def start_reading():
    """Inicia la lectura del peso."""
    global running
    running = True
    threading.Thread(target=read_weight, daemon=True).start()

def stop_reading():
    """Detiene la lectura del peso."""
    global running
    running = False

def reset_scale():
    """Resetea la balanza a cero."""
    #hx.zero()
    weight_label.config(text="Peso: 0.00")
    weight_label.config(fg="black")

def read_weight():
    """Lee el peso de la balanza y actualiza la etiqueta."""
    global reading
    while running:
        try:
            reading = 0.90#hx.get_data_mean(10)
            if reading is not None:
                # Actualiza el texto con el peso y cambia el color
                weight_label.config(text=f"Peso: {reading:.2f} kg")
                if reading < 0:  # Evitar lecturas negativas
                    weight_label.config(fg="red")
                else:
                    weight_label.config(fg="green")
            else:
                weight_label.config(text="Peso: Error de lectura", fg="red")
            time.sleep(0.5)
        except Exception as e:
            messagebox.showerror("Error", f"Se produjo un error: {e}")
            stop_reading()

def on_close():
    """Maneja el evento de cierre de la ventana."""
    stop_reading()
    #GPIO.cleanup()
    root.destroy()

def ingreso_cafe():
    #cambiar por la variable que 
    #reading = 1.2
    if reading < 0.15:
        messagebox.showerror('Ingreso de café', f"El peso actual del café es de: {reading} Kg, Por favor ingrese más café" )
    elif reading > 0.15 and reading < 1.1:
        messagebox.askokcancel('Ingreso de café', f"El peso actual del café es de: {reading} Kg, ¿seguro que quiere ingresarlo?" )
    elif reading > 1.1:
        messagebox.showerror('Ingreso de café', f"El peso actual del café es de: {reading} Kg, por favor retire café")
class SlidePanel(ttk.Frame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master=parent,relief='solid',style='DARK')

        #atributos generales
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.width = abs(start_pos - end_pos)
        print(self.width)

        #place
        self.place(relx = self.start_pos, rely = 0, relwidth = self.width, relheight = 1)

# Función para cambiar la imagen según la selección
class PanelLateralDown(ttk.Frame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master=parent,relief='raised',style='DARK')

        #atributos generales
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.width = abs(start_pos - end_pos)
        print(self.width)

        #place
        self.place(relx = self.start_pos, rely = 0.5, relwidth = self.width, relheight = 0.5)

class NotebookFrame(ttk.Notebook):
    """Clase para el Notebook con dos pestañas."""
    def __init__(self, parent):
        super().__init__(master=parent)
        self.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)

        # Crear pestañas
        self.create_tabs()

    def create_tabs(self):
        """Crea las pestañas del Notebook."""
        tab1 = tk.Frame(self, bg="lightblue", relief="groove", borderwidth=2)
        tab2 = tk.Frame(self, bg="lightgreen", relief="groove", borderwidth=2)

        # Añadir pestañas
        self.add(tab1, text="Grafica Velocidad")
        self.add(tab2, text="Tiempo de espera")



def cambiar_imagen(event):
    opcion = combo_box.get()
    print(opcion)
    ruta_imagen = rutas_imagenes.get(opcion, None)
    if ruta_imagen:
                imagen = Image.open(ruta_imagen)
                imagen = imagen.resize((150, 150))  # Cambia las dimensiones según necesites
                img_tk = ImageTk.PhotoImage(imagen)

                # Actualizar el label
                label_imagen.configure(image=img_tk, text="")  # Borra el texto si había alguno
                label_imagen.Image = img_tk  # Guarda la referencia de la imagen para evitar que sea recolectada por el Garbage Collector
                #print(f"Selección: {opcion}")
                #print(f"Ruta: {ruta_imagen}")


# Diccionario que almacena las rutas de las imágenes
rutas_imagenes = {
            "TUESTE CLARO": r"C:/Users/EQUIPO/Documents/11vo/TT/PRUEBAS/interfazPyqt6/qtCreator/pruebaProyecto/TC.png",
            "TUESTE MEDIO": r"C:/Users/EQUIPO/Documents/11vo/TT/PRUEBAS/interfazPyqt6/qtCreator/pruebaProyecto/TM.png",
            "TUESTE OBSCURO": r"C:/Users/EQUIPO/Documents/11vo/TT/PRUEBAS/interfazPyqt6/qtCreator/pruebaProyecto/TO.png",
            "TUESTE ARTESANAL": r"C:/Users/EQUIPO/Documents/11vo/TT/PRUEBAS/interfazPyqt6/qtCreator/pruebaProyecto/TA.png",
        }

# Crear la ventana principal
#ctk.CTK

#TTK Boostrap
root = ttk.Window(themename = 'superhero')
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

label_imagen = ttk.Label(panelLateral, text="", anchor="center", bootstyle='DARK')  # Asegúrate de usar un label sin texto por defecto
label_imagen.pack(pady=20)
#ttk.Label(panelIzqAbajo, background='yellow').pack(expand=True,fill="both")

# Iniciar la aplicación
root.mainloop()


