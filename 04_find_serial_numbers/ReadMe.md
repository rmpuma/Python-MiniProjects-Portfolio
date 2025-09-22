Serial Number Finder (Python)
Este proyecto consiste en un script en Python que recorre recursivamente un directorio específico para buscar números de serie dentro de archivos de texto. 
El patrón buscado es un número de serie con el formato NXXX-12345, donde N es una letra fija, XXX son tres letras y 12345 son cinco dígitos.
Es un mini proyecto ideal para practicar manejo de archivos, expresiones regulares, y procesamiento básico de datos en Python.

Objetivo del proyecto:
- El objetivo principal es practicar conceptos fundamentales de programación en Python, tales como:
- Recorrido de directorios y archivos con os.walk()
- Uso de expresiones regulares (re) para buscar patrones en texto
- Manejo de fechas y tiempo con datetime y time
- Uso de listas para almacenar resultados
- Presentación ordenada de resultados en consola

Características:
- Búsqueda recursiva en todas las subcarpetas y archivos de una ruta definida
- Reconocimiento de números de serie con formato específico usando regex
- Reporte en consola con:
    - Fecha de ejecución
    - Lista de archivos que contienen números de serie
    - Números de serie encontrados
    - Duración total de la búsqueda (en segundos, redondeada hacia arriba)
- Código simple, claro y fácil de modificar para otras búsquedas
