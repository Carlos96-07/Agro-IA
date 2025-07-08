import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
from PIL import Image

st.set_page_config(page_title="AgroIA", layout="wide")
st.title("🌱 Asistente Inteligente para Cultivos")

opcion = st.sidebar.selectbox(
    "Selecciona un módulo",
    [
        "Clasificación de hojas (CNN)",
        "Predicción de rendimiento (RNN)",
        "Recomendación de acciones (ANN)",
    ]
)

# Cargar modelos solo si se necesitan
if opcion == "Clasificación de hojas (CNN)":
    st.subheader("Clasificación de hoja sana o enferma")
    uploaded_file = st.file_uploader("Sube una imagen de hoja", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file).resize((150, 150))
        st.image(image, caption="Imagen subida", use_container_width=True) 

        model = tf.keras.models.load_model("models/cnn_mini_model.h5")

        img_array = np.array(image) / 255.0
        img_array = img_array.reshape((1, 150, 150, 3)) 

        prediction = model.predict(img_array)
        label = "Sana" if prediction[0][0] > 0.5 else "Enferma"
        st.success(f"Resultado: {label} (Confianza: {prediction[0][0]:.2f})")

elif opcion == "Predicción de rendimiento (RNN)":
    st.subheader("Predicción de rendimiento en kg")
    model = tf.keras.models.load_model("models/rnn_rendimiento.keras")

    temp_max = st.slider("Temperatura máxima", 20.0, 40.0, 30.0)
    temp_min = st.slider("Temperatura mínima", 10.0, 25.0, 20.0)
    humedad = st.slider("Humedad (%)", 50, 100, 80)
    lluvia = st.slider("Lluvia (mm)", 0.0, 50.0, 15.0)

    if st.button("Predecir rendimiento"):
        input_data = np.array([[[temp_max, temp_min, humedad, lluvia]]])
        prediction = model.predict(input_data)
        st.success(f"Rendimiento estimado: {prediction[0][0]:.2f} kg")

elif opcion == "Recomendación de acciones (ANN)":
    st.subheader("Recomendación de acción agrícola")
    model = tf.keras.models.load_model("models/ann_recomendador.keras")

    lluvia_mm = st.slider("Lluvia (mm)", 0.0, 50.0, 12.0)
    temp_max = st.slider("Temp. Máxima (°C)", 20.0, 40.0, 30.0)
    temp_min = st.slider("Temp. Mínima (°C)", 10.0, 25.0, 19.0)
    humedad = st.slider("Humedad (%)", 40, 100, 85)
    ph_suelo = st.slider("pH del suelo", 4.0, 8.0, 6.5)
    dia_del_ano = st.slider("Día del año", 1, 365, 100)

    if st.button("Recomendar acción"):
        X_input = np.array([[lluvia_mm, temp_max, temp_min, humedad, ph_suelo, dia_del_ano]])
        y_pred = model.predict(X_input)
        clases = ['riego', 'fertilizacion', 'poda']
        resultado = clases[np.argmax(y_pred)]
        st.success(f"Recomendación: {resultado}")
