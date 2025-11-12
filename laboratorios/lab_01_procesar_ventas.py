# Archivo: lab_01_procesar_ventas.py
"""
Laboratorio 1: Procesamiento de Archivo de Ventas
Objetivo: Practicar la lectura y escritura de archivos procesando un log de ventas

La función debe:
1. Leer un archivo de ventas con formato: fecha,producto,cantidad,precio
2. Calcular el total de ventas por producto
3. Generar un reporte con los resultados
"""
import pandas as pd
def procesar_ventas(archivo_entrada, archivo_salida):
    """
    Procesa un archivo de ventas y genera un reporte
    Args:
        archivo_entrada (str): Ruta del archivo de ventas
        archivo_salida (str): Ruta donde guardar el reporte
    Returns:
        dict: Resumen de ventas por producto
    Raises:
        NotImplementedError: Cuando el estudiante aún no implementa
        IOError: Cuando hay problemas con los archivos
    """
    ventas_por_producto = {}
    # TODO: Implementar el procesamiento siguiendo estos pasos:
    # 1. Leer el archivo de ventas línea por línea
#   with open(archivo_entrada, "r") as archivo:
#       for linea in archivo:
    # 2. Por cada línea:
    #    - Separar los campos (fecha,producto,cantidad,precio)
#           fecha, producto, cantidad, precio = linea.strip().split(',')
            
    #    - Calcular el total (cantidad * precio)
#           cantidad = int(cantidad)
#           precio = float(precio)
#           total=cantidad*precio
    #    - Acumular las ventas por producto
#           if producto in ventas_por_producto:
#               ventas_por_producto[producto]['cantidad'] += cantidad
#               ventas_por_producto[producto]['total'] += total
#           else:
#               ventas_por_producto[producto] = {
#                   'cantidad': cantidad,
#                  'total': total
#               }

    df = pd.read_csv(archivo_entrada,header=None, names=["fecha", "producto", "cantidad", "precio"])
    df['cantidad'] = df['cantidad'].astype(int)
    df['precio'] = df['precio'].astype(float)
    df['total'] = df['cantidad'] * df['precio']

    resumen = df.groupby('producto').agg({'cantidad': 'sum', 'total': 'sum'}).reset_index()

    # Construir diccionario de salida
    ventas_por_producto = {
        row['producto']: {'cantidad': int(row['cantidad']), 'total': float(row['total'])}
        for _, row in resumen.iterrows()
    }

    # 3. Generar el reporte con los totales
    with open(archivo_salida, "w") as archivo:
        archivo.write("<<< Reporte de Ventas >>>\n\n")
        total = 0
        for producto, informacion in ventas_por_producto.items():
            nueva_linea = f" - Producto {producto}\n"
            nueva_linea += f"   + unidades vendidas {informacion['cantidad']}\n"
            nueva_linea += f"   + total vendido del producto  ${informacion['total']:,.2f}\n\n"
            archivo.write(nueva_linea)
            total += informacion['total']
        archivo.write(f"\nTotal Vendido ${total:,.2f}")
        


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
            
    except NotImplementedError as e:
        print(f"\nError: {str(e)}")
    except IOError as e:
        print(f"\nError de archivo: {str(e)}")

if __name__ == "__main__":
    main()