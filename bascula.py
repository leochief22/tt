import RPi.GPIO as GPIO
from hx711 import HX711  # Asegúrate de tener instalada esta librería

GPIO.setmode(GPIO.BCM)

# Configura los pines de la balanza
hx = HX711(dout_pin=2, pd_sck_pin=3)

# Hacer cero de la balanza
hx.zero()

try:
    while True:
        # Obtener el promedio de las últimas lecturas
        reading = hx.get_data_mean(10)  # Puedes ajustar el número de lecturas para promediar
        print(f"Lectura: {reading}")

except KeyboardInterrupt:
    print("Proceso interrumpido por el usuario.")

finally:
    GPIO.cleanup()  # Limpiar los pines GPIO cuando termine el programa


