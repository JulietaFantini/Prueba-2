import streamlit as st

def pantalla_1_prompt():
    st.title("🎨 Generador de Prompts para Imágenes con IA: Pantalla 1 🚀")
    st.write("Responde las siguientes preguntas para definir los parámetros de tu imagen ideal.")

    # Divider for sections
    st.markdown("---")

    # Idea inicial
    st.header("🔄 ¿Ya tenés una idea inicial?")
    idea_inicial = st.text_area(
        "Escribí tu idea inicial aquí (opcional):",
        placeholder="Ejemplo: Quiero una imagen de una ciudad futurista iluminada por neón.",
        key=f"idea_inicial_{id(st)}"
    )
    if not idea_inicial:
        st.info("Aunque una idea inicial puede ser suficiente, te sugerimos explorar los parámetros adicionales para obtener un resultado más personalizado.")

    st.markdown("---")

    # Objeto principal
    st.header("📌 Objeto principal 🖑")
    objeto_principal = st.text_input(
        "¿Qué elemento o sujeto será el centro de la imagen?",
        placeholder="Ejemplo: un tigre, un rascacielos con diseño futurista.",
        key=f"objeto_principal_{id(st)}"
    )

    st.markdown("---")

    # Contexto o entorno
    st.header("🏞️ Contexto o entorno 🖑")
    contexto_opciones = ["Ciudad distópica", "Paisaje extraterrestre", "Interior minimalista", "Bosque mágico", "Paisaje histórico", "Playa tropical", "Montaña cubierta de nieve", "Espacio sideral", "Fondo abstracto", "Otro"]
    contexto = st.selectbox(
        "¿En qué tipo de ambiente o escenario se encontrará el objeto principal?",
        contexto_opciones,
        key=f"contexto_{id(st)}"
    )
    if contexto == "Otro":
        contexto_otro = st.text_input("Especificá el contexto:", key=f"contexto_otro_{id(st)}")

    st.markdown("---")

    # Nivel de complejidad
    st.header("🔧 Nivel de complejidad 🖑")
    nivel_complejidad = st.selectbox(
        "¿Qué nivel de complejidad debería tener la composición?",
        ["Básico", "Moderado", "Alto", "Extremo", "Otro"],
        key=f"nivel_complejidad_{id(st)}"
    )
    if nivel_complejidad == "Otro":
        nivel_complejidad_otro = st.text_input("Especificá el nivel de complejidad:", key=f"nivel_complejidad_otro_{id(st)}")

    st.markdown("---")

    # Botón para confirmar y continuar
    if st.button("Confirmar y continuar a la pantalla 2: recomendación de herramientas", key=f"boton_continuar_{id(st)}"):
        st.experimental_set_query_params(pantalla="2")
        st.success("¡Datos enviados correctamente!")

pantalla_1_prompt()
