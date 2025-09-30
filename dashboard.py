import streamlit as st
import pandas as pd
from utils import cargar_datos, limpiar_datos

# ======================
# CARGA DE DATOS
# ======================
df = cargar_datos("./PF_GRUPO_01.csv")
df = limpiar_datos(df)

# Asegurar que las columnas existan
if "Fecha" in df.columns:
    df["Fecha"] = pd.to_datetime(df["Fecha"], errors="coerce")

# Crear columna Total_Venta si no existe
if "Total_Venta" not in df.columns and {"Precio", "Unidades vendidas"}.issubset(df.columns):
    df["Total_Venta"] = df["Precio"] * df["Unidades vendidas"]

# ======================
# TÍTULO
# ======================
st.title("📊 Dashboard de Ventas - Pastelería")

# ======================
# INDICADORES (KPIs)
# ======================
if not df.empty:
    st.subheader("Indicadores Clave")
    col1, col2, col3 = st.columns(3)
    col1.metric("Ingresos Totales", f"S/. {df['Total_Venta'].sum():,.2f}")
    col2.metric("Unidades Vendidas", int(df["Unidades vendidas"].sum()))
    col3.metric("Precio Promedio", f"S/. {df['Precio'].mean():.2f}")
else:
    st.warning("⚠️ No hay datos disponibles en el archivo CSV.")

# ======================
# FILTROS
# ======================
if "Categoría" in df.columns:
    categorias = st.multiselect(
        "Selecciona Categorías",
        df["Categoría"].dropna().unique(),
        default=list(df["Categoría"].dropna().unique())
    )
    df_filtrado = df[df["Categoría"].isin(categorias)]
else:
    st.error("❌ La columna 'Categoría' no existe en el dataset.")
    df_filtrado = df

# ======================
# GRÁFICO POR CATEGORÍA
# ======================
st.subheader("Ventas Totales por Categoría")
if not df_filtrado.empty:
    ventas_categoria = df_filtrado.groupby("Categoría")["Total_Venta"].sum()
    if not ventas_categoria.empty:
        st.bar_chart(ventas_categoria)
    else:
        st.warning("⚠️ No hay ventas registradas para las categorías seleccionadas.")
else:
    st.warning("⚠️ No hay datos después de aplicar los filtros.")

# ======================
# TENDENCIA DE VENTAS
# ======================
st.subheader("Tendencia de Ventas por Mes")
if not df_filtrado.empty and "Fecha" in df_filtrado.columns:
    ventas_mensuales = df_filtrado.groupby(df_filtrado["Fecha"].dt.to_period("M"))["Total_Venta"].sum()
    ventas_mensuales.index = ventas_mensuales.index.astype(str)
    if not ventas_mensuales.empty:
        st.line_chart(ventas_mensuales)
    else:
        st.warning("⚠️ No hay ventas registradas en el periodo seleccionado.")
else:
    st.warning("⚠️ No se pudo generar la tendencia porque faltan datos de fecha.")
