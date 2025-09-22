import os
import re
import datetime
import time 
import math

hoy = datetime.datetime.now().date()
ruta = [ruta]

patron = r'N[a-zA-Z]{3}-\d{5}'

archivo_con_serie = []
numero_serie = []

inicio = time.time()
for carpeta, subcarpeta, archivos in os.walk(ruta):
    for arch in archivos:
        ruta_archivo = os.path.join(carpeta, arch)
        texto = open(ruta_archivo, 'r', encoding='utf-8')  # Abrir el archivo
        contenido = texto.read()                            # Leer el contenido
        busqueda = re.search(patron, contenido)            # Buscar el patrón
        texto.close()                                       # Cerrar el archivo
        if busqueda:
            numero_serie.append(busqueda.group())
            archivo_con_serie.append(arch)
final = time.time()
duracion = final - inicio
valor_redondeado = math.ceil(duracion)

        
print("-"*40)
print(f'Fecha de búsqueda: {hoy}\n')
print("ARCHIVO \t\t\t NRO. SERIE")
print("-"*7 + "\t\t\t\t " + "-"*10)
indice = 0
for a in archivo_con_serie:
    print(f'{a}\t\t{numero_serie[indice]}')
    indice +=1

print("\n")
print(f'Numeros encontrados: {len(archivo_con_serie)}')
print(f'Duración de la búsqueda: {valor_redondeado} segundos')
print("-"*40)
