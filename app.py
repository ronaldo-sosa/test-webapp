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
