import streamlit as st

# Título de la aplicación
st.title('Mi Primera Aplicación Web con Streamlit')

# Mostrar un mensaje simple
st.write("¡Bienvenido a mi aplicación!")

# Hacer una simple operación
numero = st.slider("Selecciona un número:", 0, 100)
st.write("El cuadrado de tu número es:", numero ** 2)
