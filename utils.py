import pickle
import streamlit as st

def predict_precio(data):
    # Cargar el modelo previamente entrenado para predecir el tipo de flor
    model = pickle.load(open('models/iris_model.pkl', "rb"))
    # Realizar la predicción con los datos proporcionados
    predictions = model.predict(data)
    return predictions

