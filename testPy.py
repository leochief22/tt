import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Crear la ventana principal
root = tk.Tk()
#root.geometry("1080x900")  # Ajustar el tamaño de la ventana

# Sección de contenido
content_frame = ttk.Frame(root)
content_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Contenedor de la tarjeta
card_frame = ttk.Frame(content_frame, relief="solid", padding=10)
card_frame.pack(fill="both", padx=10, pady=10)

# Imagen de perfil (simulada con un label, asegúrate de tener una imagen compatible)
profile_img = tk.PhotoImage(file=r"C:\Users\leope\OneDrive\Escritorio\TT\Interfaz\Imagenes\TC.png")  # Asegúrate de tener una imagen compatible
profile_label = ttk.Label(card_frame, image=profile_img)
profile_label.image = profile_img  # Guardar referencia para evitar que se elimine
profile_label.pack(pady=(0, 10))

# Texto del perfil
username_label = ttk.Label(card_frame, text="Tueste Claro", font=("Helvetica", 16, "bold"))
username_label.pack()

description_label = ttk.Label(card_frame, text="Parámetros del Perfil Seleccionado", font=("Helvetica", 10))
description_label.pack()

# Botones Inicio y Pausa
start_button = tk.Button(card_frame, text="Inicio", bg="green", fg="white", font=("Helvetica", 12, "bold"))
start_button.pack(fill="x", pady=5)

pause_button = tk.Button(card_frame, text="Pausa", bg="red", fg="white", font=("Helvetica", 12, "bold"))
pause_button.pack(fill="x", pady=5)

# Crear un contenedor de pestañas
notebook = ttk.Notebook(content_frame)

# Crear cada pestaña y su contenido
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

# Añadir las pestañas al Notebook
notebook.add(tab1, text="Temperatura")
notebook.add(tab2, text="Tiempo")
notebook.add(tab3, text="Velocidad")

# Empaquetar el Notebook para que aparezca en la ventana
notebook.pack(expand=True, fill="both")

# Contenido de la pestaña "Temperatura"
label1 = ttk.Label(tab1, text="Gráfica de Temperatura Esperada", font=("Helvetica", 14))
label1.pack(pady=10)

# Div para la gráfica
graph_frame = ttk.Frame(tab1, height=400, width=600)
graph_frame.pack(fill="both")

# Datos de la gráfica
tiempos = ['0s', '1.5 min', '3 min', '4.5 min', '6 min', '7.5 min', '9 min', '10.5 min', '12 min', '13.5 min', '15 min']
temperaturas = [170, 120, 95, 100, 115, 140, 170, 200, 240, 280, 320]

# Crear la figura para la gráfica
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)

# Graficar los datos
ax.plot(tiempos, temperaturas, marker='o', color='#1e90ff', label='Temperatura (°C)')
ax.set_title('Gráfica de Temperatura')
ax.set_xlabel('Tiempo [s]')
ax.set_ylabel('Temperatura [°C]')
ax.set_ylim(90, 320)
ax.set_xticks(tiempos)
ax.grid()
ax.legend()

# Crear un lienzo para la figura y empaquetarlo en la pestaña
canvas = FigureCanvasTkAgg(fig, master=graph_frame)
canvas.draw()
canvas.get_tk_widget().pack(fill="both", expand=True)

# Contenido de la pestaña "Tiempo"
label2 = ttk.Label(tab2, text="Contenido de Tiempo", font=("Helvetica", 14))
label2.pack(pady=10)

# Título sobre la barra de progreso
label_time_expected = ttk.Label(tab2, text="Tiempo de Esperado del Tostado", font=("Helvetica", 12))
label_time_expected.pack(pady=5)

# Barra de Progreso
progress_bar = ttk.Progressbar(tab2, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(pady=10)

# Configurar la barra de progreso (25% como ejemplo)
progress_bar["value"] = 25  # Ajusta el valor aquí según sea necesario
progress_bar["maximum"] = 100  # Valor máximo

# Marcas de tiempo
time_labels_frame = ttk.Frame(tab2)
time_labels_frame.pack(pady=5)

ttk.Label(time_labels_frame, text="0 min").pack(side="left", padx=(0, 10))
ttk.Label(time_labels_frame, text="11 min").pack(side="right", padx=(10, 0))

# Contenido de la pestaña "Velocidad"
label3 = ttk.Label(tab3, text="Contenido de la Velocidad", font=("Helvetica", 14))
label3.pack(pady=10)

# Título sobre la velocidad
label_speed_title = ttk.Label(tab3, text="Velocidad actual del tambor [RPMs]", font=("Helvetica", 12))
label_speed_title.pack(pady=5)

# Etiqueta de velocidad
speed_label = ttk.Label(tab3, text="Velocidad Promedio Esperada: 18 RPMs", font=("Helvetica", 10))
speed_label.pack(pady=5)

# Marcas de velocidad
speed_labels_frame = ttk.Frame(tab3)
speed_labels_frame.pack(pady=5)

ttk.Label(speed_labels_frame, text="0 RPMs").pack(side="left", padx=(0, 10))
ttk.Label(speed_labels_frame, text="80 RPMs").pack(side="right", padx=(10, 0))

# Carrusel de Perfiles de Tostado
carousel_frame = ttk.Frame(content_frame)
carousel_frame.pack(fill="both", padx=10, pady=10)

carousel_label = ttk.Label(carousel_frame, text="Otros perfiles de tostado", font=("Helvetica", 14))
carousel_label.pack(pady=10)

# Crear un marco para el carrusel
carousel_inner_frame = ttk.Frame(carousel_frame)
carousel_inner_frame.pack()

# Agregar imágenes al carrusel
image_paths = [
    r"C:\Users\leope\OneDrive\Escritorio\TT\Interfaz\Imagenes\TM.png",  # Reemplaza con la ruta de tu imagen
    r"C:\Users\leope\OneDrive\Escritorio\TT\Interfaz\Imagenes\TO.png",  # Reemplaza con la ruta de tu imagen
    r"C:\Users\leope\OneDrive\Escritorio\TT\Interfaz\Imagenes\TA.png"   # Reemplaza con la ruta de tu imagen
]

# Función para actualizar la imagen en el carrusel
def update_image(index):
    img = tk.PhotoImage(file=image_paths[index])
    img_label.config(image=img)
    img_label.image = img  # Guardar referencia
    current_image_index.set(index)

# Crear un label para mostrar las imágenes
img_label = ttk.Label(carousel_inner_frame)
img_label.pack(pady=10)

# Índice de la imagen actual
current_image_index = tk.IntVar(value=0)

# Botones para navegar por el carrusel
prev_button = tk.Button(carousel_inner_frame, text="Anterior", command=lambda: update_image((current_image_index.get() - 1) % len(image_paths)))
prev_button.pack(side="left", padx=5)

next_button = tk.Button(carousel_inner_frame, text="Siguiente", command=lambda: update_image((current_image_index.get() + 1) % len(image_paths)))
next_button.pack(side="right", padx=5)

# Mostrar la primera imagen
update_image(0)

# Ejecutar la aplicación
root.mainloop()

