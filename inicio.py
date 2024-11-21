import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="NASAE PROJECT",
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
        border: 2px solid #5e17eb;  /* amarillo neón */
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
       
    [data-testid=stSidebarContent] {
        background-color: #dbdbdb;
    }
        stSidebarContent {
        background-color: #dbdbdb;
    }
        .st-emotion-cache-6qob1r {
        background-color: #c9c9c9;
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
st.markdown('<h2 class="centered"> Quienes Somos?</h2>', unsafe_allow_html=True)
# Texto en recuadro amarillo
st.markdown("""
<div class='box'>
ANÓNIMOS NASAE es una empresa apasionada por transformar datos en poderosas herramientas para el éxito empresarial. Nos especializamos en la creación de soluciones personalizadas que permitan a las organizaciones tomar decisiones estratégicas e informadas, maximizando su impacto en el mercado. Al combinar innovación tecnológica, análisis de datos avanzado y visualizaciones intuitivas, convertimos la información en conocimientos prácticos que impulsan el crecimiento y solidifican el liderazgo. En ANÓNIMOS NASAE creemos que los datos son la clave para construir un futuro más inteligente. 🚀</div>""", unsafe_allow_html=True)
