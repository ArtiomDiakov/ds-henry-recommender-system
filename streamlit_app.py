import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="PROJECT 001",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Estilos personalizados
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400&display=swap');

    body {
        font-family: 'Roboto', sans-serif;
        color: white;
        margin: 0;
    }

    h1 {
        font-family: 'Tahoma', sans-serif';
        color: white;
        font-size: 60px;  /* Tamaño del título principal */
        text-align: center; /* Centrar el título */
        margin-top: 20px;  /* Espaciado superior */
    }

    .box {
        border: 2px solid #FFD700;  /* amarillo neón */
        border-radius: 15px;
        padding: 20px;
        width: 60%;  /* Hacemos el recuadro más estrecho */
        margin-top: 20px;
        font-size: 24px;
        margin: auto;
    }

    .about-title {
        font-size: 40px;
        font-weight: bold;
        color: #ffffff;  
        margin-top: 0px;
        margin-bottom: 20px;
        text-align: center;
    }

    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
        
    }
    
    [data-testid="stFullScreenFrame"]{
        margin:auto;
        max-width:300px;
       }
    </style>
""", unsafe_allow_html=True)

# Título principal de la página
st.title("ANONIMOS NASAE")

# Imagen centrada con st.image
st.markdown('<div class="centered">', unsafe_allow_html=True)
st.image("imagenes_web/logo.png")
st.markdown('</div>', unsafe_allow_html=True)

# Espacio para "About Us"
#st.markdown("<div class='about-title'>About</div>", unsafe_allow_html=True)

# Texto en recuadro amarillo
st.markdown("""
<div class='box'>
We are a data consultancy made up of five members, coming from varied areas, but with the same objective and passion: improving business processes. 
We are specialized in providing strategic solutions based on data analysis. Our goal is to support our clients in making key decisions that drive their 
growth and position them as leaders in their respective industries. We work with businesses from various sectors, including restaurants and related 
businesses, helping them optimize their operations, identify market opportunities and improve their customer experience through the intelligent use of data.
</div>
""", unsafe_allow_html=True)
