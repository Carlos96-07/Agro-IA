# AgroIA 

Asistente Inteligente para Agricultura Sostenible en Costa Rica

## Módulos:

1. Clasificación de enfermedades en hojas (CNN)
2. Predicción del rendimiento de cultivos (RNN)
3. Recomendación de acciones agrícolas (ANN)

Estructura del Proyecto:
AgroIA/
├── app/ # Interfaz Streamlit
├── models/ # Modelos entrenados (.h5 / .keras)
├── data/
│ └── raw/
│ └── mini_dataset/
│ ├── sanas/
│ └── enfermas/
├── notebooks/ # Notebooks de entrenamiento
├── src/ # Scripts de preprocesamiento y modelos
├── requirements.txt
└── README.md

 Requisitos

- Python 3.10+
- pip
- Jupyter Notebook
- Streamlit

  Pasos:
  Crea un entorno virtual: python -m venv .venv
  Windows:
  .venv\Scripts\activate
  Entrenamiento de modelos:
  jupyter notebook
  notebooks/02_CNN_Leaves.ipynb (Clasificación)
  notebooks/03_RNN_Yield.ipynb (Rendimiento)
  notebooks/04_ANN_Reco.ipynb (Recomendaciones)

  Ejecutar la aplicación Streamlit: streamlit run app/Home.py
  Navegador: http://localhost:8501

  Ver estado del entorno:
  where python  En Windows

  Modelos disponibles:
  CNN	cnn_mini_model.h5	Clasificación de hojas
  RNN	rnn_rendimiento.keras	Predicción de rendimiento
  ANN	ann_recomendador.keras	Recomendación de acción
  
Tecnologías: Python, TensorFlow, Streamlit.
