# Archivo: demo_01_archivos_basicos.py
"""
Demo 1: Operaciones Básicas con Archivos
Objetivo: Mostrar operaciones básicas de lectura y escritura de archivos en Python
"""

def demo_archivos_basicos():
    print("=== Demo: Operaciones Básicas con Archivos ===")
    
    # Ejemplo 1: Escribir en un archivo
    print("\n1. Escribiendo en un archivo:")
    try:
        with open("ventas.txt", "w") as archivo:
            archivo.write("Laptop,1200\n")
            archivo.write("Smartphone,800\n")
            archivo.write("Tablet,500\n")
        print("Archivo creado exitosamente")
    except IOError as e:
        print(f"Error al escribir archivo: {e}")
    
    # Ejemplo 2: Leer un archivo completo
    print("\n2. Leyendo archivo completo:")
    try:
        with open("ventas.txt", "r") as archivo:
            contenido = archivo.read()
            print("Contenido del archivo:")
            print(contenido)
    except IOError as e:
        print(f"Error al leer archivo: {e}")
    
    # Ejemplo 3: Leer archivo línea por línea
    print("\n3. Leyendo archivo línea por línea:")
    # "r" = read lectura
    # "w" = write escritura
    # "a" = append agregar al final
    try:
        with open("ventas.txt", "r") as archivo:
            print("Procesando ventas:")
            total = 0
            for linea in archivo:
                producto, precio = linea.strip().split(",") # producto=Tablet precio=500
                total += float(precio)  # total = 0 + 1200 = 1200 + 800 = 2000 + 500 = 2500
                print(f"- {producto}: ${precio}")
            print(f"Total de ventas: ${total}")
    except IOError as e:
        print(f"Error al procesar archivo: {e}")
    
    # Ejemplo 4: Agregar contenido al archivo
    print("\n4. Agregando contenido al archivo:")
    try:
        with open("ventas.txt", "a") as archivo:
            archivo.write("Auriculares,100\n")
        print("Contenido agregado exitosamente")
        
        # Mostrar archivo actualizado
        with open("ventas.txt", "r") as archivo:
            print("Archivo actualizado:")
            print(archivo.read())
    except IOError as e:
        print(f"Error al actualizar archivo: {e}")

if __name__ == "__main__":
    demo_archivos_basicos()