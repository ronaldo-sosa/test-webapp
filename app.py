import streamlit as st

# Título de la aplicación
st.title('Eres la mujer de mis sueños, Jimena')

# Mostrar un mensaje simple
st.write("¡Nos quedan 7 días para vernos!")

# Hacer una simple operación
st.write('Solo ando probando esto, jeje.')
st.write('holaaaa')
numero = st.slider("Selecciona un número:", 0, 100)
st.write("El cuadrado de tu número es:", numero ** 2)

from datetime import datetime

# Título de la aplicación
st.title("Aplicación con Selección de Fecha")

# Mostrar el calendario y permitir al usuario seleccionar una fecha
fecha_seleccionada = st.date_input(
    "Selecciona una fecha", 
    value=datetime.today(),  # Fecha predeterminada es la fecha actual
    min_value=datetime(2024, 10, 1),  # Fecha mínima
    max_value=datetime(2025, 10, 20)  # Fecha máxima
)

# Mostrar la fecha seleccionada
st.write("Has seleccionado:", fecha_seleccionada)
