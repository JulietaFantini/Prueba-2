import streamlit as st
import pandas as pd
import os

# Verificar si los archivos están disponibles
def verificar_archivos():
    archivos = [
        r"C:\\Users\\Juli\\Tabla_Ajustada_con_ejemplo_cultural_separado.xlsx",
        r"C:\\Users\\Juli\\Cuadro_Completo_de_Herramientas_de_IA_para_Generaci_n_de_Im_genes.xlsx"
    ]

    for archivo in archivos:
        if not os.path.exists(archivo):
            st.error(f"Archivo no encontrado: {archivo}")
        else:
            st.write(f"Archivo encontrado: {archivo}")

verificar_archivos()

# Cargar las bases de datos
@st.cache_data
def cargar_datos():
    try:
        tabla_estilos = pd.read_excel(r"C:\\Users\\Juli\\Tabla_Ajustada_con_ejemplo_cultural_separado.xlsx")
        cuadro_herramientas = pd.read_excel(r"C:\\Users\\Juli\\Cuadro_Completo_de_Herramientas_de_IA_para_Generaci_n_de_Im_genes.xlsx")
        return tabla_estilos, cuadro_herramientas
    except FileNotFoundError as e:
        st.error(f"No se encontró uno de los archivos necesarios: {e}")
        return None, None

tabla_estilos, cuadro_herramientas = cargar_datos()

def pantalla_2_recomendaciones():
    st.title("✨ Recomendaciones de Herramientas de IA para tus Imágenes 🚀")

    # Verificar si los parámetros de la pantalla 1 están en session_state
    if "idea_inicial" not in st.session_state:
        st.error("No se encontraron datos de la pantalla 1. Por favor, completa la pantalla 1 primero.")
        return

    # Resumen de los parámetros ingresados
    st.header("🔎 Resumen de tus parámetros")
    idea_inicial = st.session_state.get("idea_inicial", "No especificado")
    objeto_principal = st.session_state.get("objeto_principal", "No especificado")
    contexto = st.session_state.get("contexto", "No especificado")
    nivel_complejidad = st.session_state.get("nivel_complejidad", "No especificado")
    plano_fotografico = st.session_state.get("plano_fotografico", "No especificado")
    detalles = st.session_state.get("detalles", "No especificado")
    estilo = st.session_state.get("estilo", "No especificado")
    proposito = st.session_state.get("proposito", "No especificado")

    st.write(f"- **Idea inicial:** {idea_inicial}")
    st.write(f"- **Objeto principal:** {objeto_principal}")
    st.write(f"- **Contexto:** {contexto}")
    st.write(f"- **Nivel de complejidad:** {nivel_complejidad}")
    st.write(f"- **Plano fotográfico:** {plano_fotografico}")
    st.write(f"- **Características adicionales:** {detalles}")
    st.write(f"- **Estilo:** {estilo}")
    st.write(f"- **Propósito:** {proposito}")

    st.markdown("---")

    # Recomendación principal: ChatGPT con DALL·E
    st.header("⭐ Recomendación Principal")
    st.write("Por defecto, recomendamos **ChatGPT** con **DALL·E** para generar imágenes de alta calidad basadas en texto.")
    st.write("Ideal para: versatilidad, rapidez y generación en múltiples estilos.")
    st.markdown("[Probar ChatGPT con DALL·E](https://chat.openai.com/) 🖼️")

    st.markdown("---")

    # Filtrar herramientas según parámetros
    st.header("🔧 Otras herramientas recomendadas")

    herramientas_filtradas = tabla_estilos[
        (tabla_estilos["Estilo"] == estilo) & 
        (tabla_estilos["Usos Asociados"].str.contains(proposito, na=False))
    ]

    if not herramientas_filtradas.empty:
        for _, row in herramientas_filtradas.iterrows():
            st.subheader(row["Herramientas Asociadas"])
            st.write(f"- **Descripción breve:** {row['Descripción Breve']}")
            st.write(f"- **Usos asociados:** {row['Usos Asociados']}")
            st.write(f"- **Ejemplo cultural:** {row['Ejemplo Cultural']}")
            st.markdown(f"[Probar herramienta](https://www.google.com/search?q={row['Herramientas Asociadas'].replace(' ', '+')})")
            st.markdown("---")
    else:
        st.write("No se encontraron herramientas específicas para tu combinación de estilo y propósito. Intenta con ChatGPT + DALL·E como opción versátil.")

    # Agregar filtros interactivos
    st.header("🔍 Explora herramientas por filtros adicionales")
    filtro_estilo = st.selectbox("Filtrar por estilo:", tabla_estilos["Estilo"].unique(), key="filtro_estilo")
    herramientas_filtradas_filtro = tabla_estilos[tabla_estilos["Estilo"] == filtro_estilo]

    if not herramientas_filtradas_filtro.empty:
        for _, row in herramientas_filtradas_filtro.iterrows():
            st.subheader(row["Herramientas Asociadas"])
            st.write(f"- **Descripción breve:** {row['Descripción Breve']}")
            st.write(f"- **Usos asociados:** {row['Usos Asociados']}")
            st.write(f"- **Ejemplo cultural:** {row['Ejemplo Cultural']}")
            st.markdown(f"[Probar herramienta](https://www.google.com/search?q={row['Herramientas Asociadas'].replace(' ', '+')})")
            st.markdown("---")
    else:
        st.write("No se encontraron herramientas para el estilo seleccionado.")

    # Enlace a explorar más herramientas
    st.markdown("[Explorar más herramientas de IA](https://www.stablediffusionweb.com/) 🌐")

pantalla_2_recomendaciones()
