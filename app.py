import json
from PIL import Image
import pandas as pd
import streamlit as st
from streamlit_lottie import st_lottie
from textblob import TextBlob

# Función para cargar el archivo JSON local
def load_lottiefile(filepath: str):
  with open(filepath, "r") as f:
    return json.load(f)


st.title("Análisis de Sentimiento, parchate y responde, no hay respuestas buenas ni malas")

# Cargar y mostrar la animación Lottie (JSON)
lottie_anim = load_lottiefile("Juggling ball.json")
st_lottie(lottie_anim, height=300, key="juggling")

st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")
with st.expander('Analizar texto'):
    text = st.text_input('Escribe por favor: ')
    if text:

        translation = translator.translate(text, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))
        x=round(blob.sentiment.polarity,2)
        if x > 0.0 and x <=1.0:
            st.write( 'Es un sentimiento Positivo 😊')
        elif x >=-1 and x <= 0:
            st.write( 'Es un sentimiento Negativo 😔')
        else:
            st.write( 'Es un sentimiento Neutral 😐')
