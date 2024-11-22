import streamlit as st

st.markdown("""
    <style>
    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Nube de Palabras")
st.markdown('<div class="centered">', unsafe_allow_html=True)
st.image("imagenes_web/wordcloud_reviews.png")
st.markdown('</div>', unsafe_allow_html=True)