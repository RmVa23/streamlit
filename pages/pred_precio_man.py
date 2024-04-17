import streamlit as st
import pandas as pd
from utils import predict_precio

# Título de la aplicación
st.title('Predicción manual de flores')
st.image('coche.jpg', caption='Imagen de coche', use_column_width=True)

# Texto introductorio
st.write('**Ingresa los datos manualmente para realizar la predicción del precio:**')

# Diccionario para almacenar los datos de entrada
input_data = {}

# Lista de columnas para las características del coche y el área
columns = ['País', 'Ciudad', 'Tipo de vehículo', 'Marca del vehículo', 'Gama', 'Híbrido']

# Diccionario con las opciones para cada característica
options = {
    'País': ['España', 'Francia', 'Italia', 'Alemania', 'Austria', 'Suiza', 'Gran Bretaña', 'Polonia', 'Grecia', 'Países Bajos', 'Rumanía', 'Noruega', 'Suecia', 'Dinamarca', 'letonia', 'Lituania', 'Hungría'],
    'Tipo de vehículo': ['Sedán', 'SUV', 'Coupé', 'Pick-up'],
    'Marca del vehículo': ['Toyota', 'Honda', 'Ford', 'Lexus', 'BMW', 'Audi', 'Citroen', 'Volkswagen', 'Hyundai'],
    'Gama': ['Alta', 'Media', 'Baja'],
    'Híbrido': ['Sí', 'No']
}

# Ciudad se introduce manualmente
input_data['Ciudad'] = st.text_input('Ciudad')

# Bucle para recorrer las columnas y obtener los datos de entrada
for col in options.keys():
    # Widget de selección de opciones para todas las características excepto la ciudad
    if col != 'Ciudad':
        input_data[col] = st.selectbox(col, options[col])


# Botón para realizar la predicción
if st.button('Realizar Predicción'):
    # Convertir el diccionario de entrada a un DataFrame de una sola fila
    input_df = pd.DataFrame([input_data])

    # Realizar la predicción utilizando la función predict_flores
    predicted_value = predict_flores(input_df)

    # Mostrar el resultado de la predicción
    st.success('Éxito al realizar la predicción!')
    st.write('El resultado de la predicción es:', predicted_value[0])
