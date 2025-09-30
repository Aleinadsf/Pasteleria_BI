import pandas as pd

# funcion una para cargar los datos
def cargar_datos(ruta):
    return pd.read_csv(ruta)

# Funciones reutilizables (limpieza de datos, carga, filtrado)
def limpiar_datos(df):
    df = df.dropna(subset=['Precio', 'Unidades vendidas'])
    df['Precio'] = pd.to_numeric(df['Precio'], errors='coerce')
    df['Unidades vendidas'] = pd.to_numeric(df['Unidades vendidas'], errors='coerce')
    df['Total_Venta'] = df['Precio'] * df['Unidades vendidas']
    return df

def calcular_kpis(df):
    ticket_promedio = df["Total_Venta"].sum() / len(df)
    top_productos = df.groupby("Producto")["Total_Venta"].sum().sort_values(ascending=False).head(5)
    print("\n--- KPIs ---")
    print(f"🎯 Ticket promedio: S/. {ticket_promedio:.2f}")
    print("🥇 Top 5 productos más vendidos por ingresos:")
    print(top_productos)
    
def exportar_reporte(df):
    df.to_excel("reporte_ventas.xlsx", index=False)
    print("📂 Reporte exportado: reporte_ventas.xlsx")
