# Archivo: lab_01_procesar_ventas_solucion.py
"""
Laboratorio 1: Procesamiento de Archivo de Ventas (SOLUCIÓN)
Objetivo: Practicar la lectura y escritura de archivos procesando un log de ventas
"""

def procesar_ventas(archivo_entrada, archivo_salida):
    """
    Procesa un archivo de ventas y genera un reporte
    Args:
        archivo_entrada (str): Ruta del archivo de ventas
        archivo_salida (str): Ruta donde guardar el reporte
    Returns:
        dict: Resumen de ventas por producto
    Raises:
        IOError: Cuando hay problemas con los archivos
    """
    # Diccionario para almacenar totales por producto
    ventas_por_producto = {}
    
    # Leer archivo de ventas
    with open(archivo_entrada, "r") as archivo:
        for linea in archivo:
            # Separar campos
            fecha, producto, cantidad, precio = linea.strip().split(",")
            
            # Convertir a números
            cantidad = int(cantidad)
            precio = float(precio)
            total = cantidad * precio
            
            # Actualizar totales
            if producto in ventas_por_producto:
                ventas_por_producto[producto]['cantidad'] += cantidad
                ventas_por_producto[producto]['total'] += total
            else:
                ventas_por_producto[producto] = {
                    'cantidad': cantidad,
                    'total': total
                }
    
    # Generar reporte
    with open(archivo_salida, "w") as archivo:
        archivo.write("=== Reporte de Ventas ===\n\n")
        
        gran_total = 0
        for producto, datos in ventas_por_producto.items():
            linea = f"{producto}:\n"
            linea += f"  Unidades vendidas: {datos['cantidad']}\n"
            linea += f"  Total ventas: ${datos['total']:.2f}\n\n"
            archivo.write(linea)
            gran_total += datos['total']
        
        archivo.write(f"Total general: ${gran_total:.2f}\n")
    
    return ventas_por_producto

def main():
    # Crear archivo de prueba
    datos_prueba = [
        "2024-02-01,Laptop,2,1200\n",
        "2024-02-01,Smartphone,1,800\n",
        "2024-02-02,Laptop,1,1200\n",
        "2024-02-02,Tablet,3,500\n"
    ]
    
    try:
        # Crear archivo de ventas
        with open("ventas.txt", "w") as archivo:
            archivo.writelines(datos_prueba)
        
        print("=== Procesamiento de Archivo de Ventas ===")
        print("\nContenido del archivo de ventas:")
        print("".join(datos_prueba))
        
        # Procesar ventas
        resultados = procesar_ventas("ventas.txt", "reporte_ventas.txt")
        
        print("\nReporte generado. Contenido:")
        with open("reporte_ventas.txt", "r") as archivo:
            print(archivo.read())
            
    except IOError as e:
        print(f"\nError de archivo: {str(e)}")

if __name__ == "__main__":
    main()