# Archivo: demo_02_formatos.py
"""
Demo 2: Trabajando con Formatos de Archivo
Objetivo: Mostrar el manejo de archivos CSV y JSON en Python
"""

import csv
import json
from datetime import datetime

def demo_formatos():
    print("=== Demo: Trabajando con Formatos de Archivo ===")
    
    # Ejemplo 1: Escribir archivo CSV
    print("\n1. Escribiendo archivo CSV:")
    productos = [
        ['id', 'nombre', 'precio', 'stock'],
        ['1', 'Laptop Pro', '1200', '5'],
        ['2', 'Smartphone X', '800', '10'],
        ['3', 'Tablet Air', '500', '8']
    ]
    
    try:
        with open('inventario.csv', 'w', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerows(productos)
        print("Archivo CSV creado exitosamente")
    except IOError as e:
        print(f"Error al escribir CSV: {e}")
    
    # Ejemplo 2: Leer archivo CSV
    print("\n2. Leyendo archivo CSV:")
    try:
        with open('inventario.csv', 'r') as archivo:
            reader = csv.DictReader(archivo)
            print("Inventario actual:")
            for row in reader:
                print(f"- {row['nombre']}: ${row['precio']} ({row['stock']} unidades)")
    except IOError as e:
        print(f"Error al leer CSV: {e}")
    
    # Ejemplo 3: Crear archivo JSON
    print("\n3. Escribiendo archivo JSON:")
    ventas = {
        'fecha': datetime.now().strftime('%Y-%m-%d'),
        'total': 2500,
        'transacciones': [
            {'producto': 'Laptop Pro', 'cantidad': 1, 'total': 1200},
            {'producto': 'Smartphone X', 'cantidad': 2, 'total': 1300}
        ]
    }
    
    try:
        with open('ventas.json', 'w') as archivo:
            json.dump(ventas, archivo, indent=4)
        print("Archivo JSON creado exitosamente")
    except IOError as e:
        print(f"Error al escribir JSON: {e}")
    
    # Ejemplo 4: Leer archivo JSON
    print("\n4. Leyendo archivo JSON:")
    try:
        with open('ventas.json', 'r') as archivo:
            datos = json.load(archivo)
            print(f"Ventas del día {datos['fecha']}:")
            print(f"Total: ${datos['total']}")
            print("Transacciones:")
            for t in datos['transacciones']:
                print(f"- {t['producto']}: {t['cantidad']} unidad(es) = ${t['total']}")
    except IOError as e:
        print(f"Error al leer JSON: {e}")

if __name__ == "__main__":
    demo_formatos()


import pandas as pd

df = pd.read_csv('/workspaces/codespaces-blank/inventario.csv')
print(df)