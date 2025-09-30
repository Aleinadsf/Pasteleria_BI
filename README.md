
# 🧁 Proyecto de Análisis de Ventas – Pastelería

## Descripción del proyecto

Este proyecto consiste en el diseño de un programa en **Python** que analiza un conjunto de datos simulados de ventas en una pastelería. El programa permite:

- Cargar los datos desde un archivo **CSV**.
- Filtrar ventas por fecha o categoría.
- Calcular estadísticas generales con **Pandas** y análisis estadístico con **NumPy**.
- Mostrar los resultados de manera organizada en consola.
- Convertir los datos en **objetos** mediante una clase `Producto`.
- Utilizar estructuras de datos como **listas, tuplas y diccionarios**.

Este proyecto cumple con los requerimientos de:

* **Estructuras repetitivas** y uso de listas.
* **Funciones y módulos** para una estructura ordenada.
* **Clases y objetos** para modelar las ventas.
* Uso de **Pandas** para manipulación de datos.
* Uso de **NumPy** para cálculos estadísticos.
* **Documentación clara** y presentación profesional.


## Estructura del proyecto

Proyecto_ventas/

├── PF_GRUPO.csv             
├── main.py                  
├── producto.py                  
├── analisis_pandas.py                  
├── analisis_numpy.py                  
├── dashboard.py                  
├── utils.py                 
├── README.md               
└── __pycache__/  



## **Requisitos previos**

Asegúrate de tener instalado:

* **Python 3.8 o superior**
* Librerías externas:
  * `pandas`
  * `numpy`
  * `matplotlib`
  * `seaborn`
  * `streamlit`

Instala las dependencias con:

- pip install pandas numpy matplotlib seaborn streamlit

## **Ejecución del programa**

Desde la raíz del proyecto, ejecuta:

- python main.py
  
De igualmanera para visualizar el dashboard se ejecuta en consola lo siguiente:

- streamlit run dashboard.py

## Funcionalidades principales

1. Carga y limpieza de datos

   * Se cargan los datos desde `PF_GRUPO.csv` usando Pandas.
   * Se agrega la columna `Total_Venta` calculada como `Precio * Unidades vendidas`.

2. Estadísticas generales (Pandas)

   * Total de productos vendidos.
   * Ingresos totales.
   * Precio promedio.
   * Producto más caro y más barato.

3. Estadísticas avanzadas (NumPy)

   * Promedio de ventas.
   * Desviación estándar.
   * Mediana, mínimo y máximo.

4. Filtros dinámicos

   * Ventas por categoría.
   * Ventas en un mes específico (ej. agosto 2025).
   * Ventas de dulces entre octubre y diciembre 2025.
   * Productos con ventas menores a S/.10.

5. Estructuras solicitadas

   * **Listas** → Conversión del DataFrame a lista de objetos `Producto`.
   * **Tuplas** → Categorías únicas y fechas únicas.
   * **Diccionarios** → Conteo de productos por categoría.



