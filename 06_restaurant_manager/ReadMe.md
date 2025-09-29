Sistema de Facturación para Restaurante (Python + Tkinter)

Este proyecto es una aplicación de escritorio desarrollada en Python utilizando la biblioteca **Tkinter**. Simula un sistema de facturación para un restaurante, 
permitiendo seleccionar productos, calcular costos, generar recibos y guardar la información.Ideal para aprender y practicar conceptos clave del desarrollo de interfaces 
gráficas con Python, como gestión de eventos, uso de variables, actualización de datos en tiempo real y diseño de ventanas interactivas.

---

## Objetivo del Proyecto
El propósito principal de este sistema es reforzar conceptos fundamentales del desarrollo de aplicaciones de escritorio con Python y **Tkinter**, tales como:

- Creación de interfaces gráficas divididas en paneles.
- Manejo de variables ligadas a widgets (`StringVar`, `IntVar`).
- Actualización dinámica de precios según la selección del usuario.
- Uso de `Checkbutton`, `Entry`, `Label` y `Button`.
- Generación de recibos personalizados.
- Guardado de información en archivos `.txt`.
- Implementación de una calculadora funcional dentro de la interfaz.

---

##  Funcionalidades Principales
- ✅ Selección de comidas, bebidas y postres mediante `Checkbutton`.
- ✅ Entrada manual de cantidades con activación dinámica de campos.
- ✅ Cálculo automático de:
  - Subtotales por categoría
  - Impuestos (7%)
  - Total general
- ✅ Generación de recibo con número único y fecha/hora.
- ✅ Opción para guardar el recibo como archivo `.txt`.
- ✅ Botón para reiniciar toda la interfaz (Reset).
- ✅ Calculadora básica integrada (suma, resta, multiplicación, división).

---

## 🖼️ Interfaz Gráfica

- Ventana fija de tamaño `1080x630`, sin opción de maximizar.
- Paneles divididos por función: comida, bebida, postres, costos, calculadora, recibo y botones de acción.
- Uso de fuentes personalizadas y colores temáticos (`burlywood`, `azure4`) para mejor experiencia visual.
