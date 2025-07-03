""" #para termopar
import time
import board
import digitalio
import adafruit_max6675

# Configuración SPI
spi = board.SPI()  # Usa SPI por defecto: CLK=11, MISO=9, MOSI=10
cs = digitalio.DigitalInOut(board.D8)  # Chip select (CS) en GPIO8

# Crear el objeto del sensor
sensor = adafruit_max6675.MAX6675(spi, cs)

def termopar_lectura():
    try:
        while True:
            temp_c = sensor.temperature
            print(f"Temperatura: {temp_c:.2f} °C")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Lectura detenida.")

    return temp_c """
# termopar.py
import time
import random  # simula valores

temp_c = 0.0

def read_temp():
    global temp_c
    temp_c = random.uniform(20, 100)  # reemplaza con sensor.temperature
    return temp_c

def get_temp():
    return temp_c
