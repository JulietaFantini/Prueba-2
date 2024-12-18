import pantalla_1_prompt
import pantalla_2_recomendaciones
import streamlit as st

# Determinar pantalla actual
pantalla_actual = st.query_params.get("pantalla", ["1"])[0]  # Cambiado a st.query_params

if pantalla_actual == "1":
    pantalla_1_prompt.pantalla_1_prompt()
elif pantalla_actual == "2":
    pantalla_2_recomendaciones.pantalla_2_recomendaciones()
