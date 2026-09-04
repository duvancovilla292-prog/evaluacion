# Evaluación Covilla Duvan: Facturación con Descuentos Especiales

## Descripción Técnica
Actualización del sistema de facturación POS en Python. Esta iteración introduce la gestión de rutas relativas para el almacenamiento estructurado de archivos, un módulo independiente para el cálculo de descuentos comerciales y una trazabilidad extendida en los registros CSV.

## Arquitectura y Novedades
*   **Gestión de Directorios (`os.path`):** Implementación de la función `obtener_ruta()` que aísla la persistencia de datos. Todos los archivos `.csv` y `.txt` se generan y consultan automáticamente dentro de un subdirectorio `data/`.
*   **Módulo de Descuentos (`descuent.py`):** Lógica encapsulada para validar la aplicación de descuentos, limitando estrictamente el ingreso a un rango numérico del 0% al 50%.
*   **Trazabilidad Financiera Extendida:** Las cabeceras de `Ventas.csv` se actualizaron para incluir el nombre del producto, el porcentaje de descuento y el valor final cobrado.

## ⚠️ Análisis de Bugs Críticos (funcionees_2.py)
En la función `FACTURA()` existen dos vulnerabilidades lógicas introducidas en esta versión:
1.  **Ruptura del Carrito (Línea 117):** El bucle `while True` para ingresar múltiples productos tiene un `break` incondicional al final de la iteración. Esto obliga al sistema a procesar solo un producto por factura.
2.  **Fallo por Variable No Definida (NameError):** La variable `k` almacena la información del producto. Si el usuario ingresa un código que no existe, el flujo cae en el bloque `else`, ejecuta el `break` incondicional e intenta escribir en `Ventas.csv` llamando a `k['nombre']`. Como `k` no fue declarada globalmente ni dentro del `else`, el programa colapsará.
