import tkinter as tk
from tkinter import messagebox
import threading
import time
import RPi.GPIO as GPIO
from hx711 import HX711  # Asegúrate de tener instalada esta librería

# Configuración de GPIO y la balanza
GPIO.setmode(GPIO.BCM)
hx = HX711(dout_pin=2, pd_sck_pin=3)
hx.zero()

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
    hx.zero()
    weight_label.config(text="Peso: 0.00")
    weight_label.config(fg="black")

def read_weight():
    """Lee el peso de la balanza y actualiza la etiqueta."""
    while running:
        try:
            reading = hx.get_data_mean(10)
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
    GPIO.cleanup()
    root.destroy()

# Crear la ventana principal
root = tk.Tk()
root.title("Lectura de Peso")
root.geometry("350x250")
root.protocol("WM_DELETE_WINDOW", on_close)

# Título de la interfaz
title_label = tk.Label(root, text="Sistema de Balanza", font=("Arial", 24))
title_label.pack(pady=10)

# Etiqueta para mostrar el peso
weight_label = tk.Label(root, text="Peso: --", font=("Arial", 18))
weight_label.pack(pady=20)

# Botones de control
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

start_button = tk.Button(frame_buttons, text="Iniciar", width=10, command=start_reading)
start_button.grid(row=0, column=0, padx=10)

stop_button = tk.Button(frame_buttons, text="Detener", width=10, command=stop_reading)
stop_button.grid(row=0, column=1, padx=10)

reset_button = tk.Button(frame_buttons, text="Reiniciar", width=10, command=reset_scale)
reset_button.grid(row=1, column=0, columnspan=2, pady=10)

# Iniciar la aplicación
root.mainloop()