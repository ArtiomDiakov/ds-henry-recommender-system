# import streamlit as st

# st.title('NASAe Restaurant Buisiness Improvement Application!')

# st.write('Please Select a buisiness and it will give you 5 key points to improve you restaurant!')


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
        background: url('imagenes_web/logo.png') no-repeat center center fixed;
        background-size: cover;
        font-family: 'Roboto', sans-serif;
        color: white;
        margin: 0;
    }

    h1 {
        font-family: 'Tahoma', sans-serif;
        color: white;
        font-size: 60px;  /* Tamaño del título principal */
        text-align: center; /* Centrar el título */
        margin-top: 20px;  /* Espaciado superior */
    }
    h3 {
        font-family: 'Tahoma', sans-serif;
        color: white;
        font-size: 40px;  /* Tamaño del título principal */
        text-align: center; /* Centrar el título */
        margin: 70px 0 50px 0;  /* Espaciado superior */

    }

    h2, h3 {
        font-family: 'Tahoma', sans-serif;
        color: white;
        
        
    }

    .title-box {
        margin-top: 40px;  /* Separación entre el título principal y el recuadro */
    }

    .box {
        border: 2px solid #FFD700;  /* amarillo neón */
        border-radius: 15px;
        padding: 20px;
        width: 60%;  /* Hacemos el recuadro más estrecho */
        margin-top: 20px;
        font-size:24px;
        margin:auto;
    }

    .about-title {
        font-size: 40px;
        font-weight: bold;
        text-align: left;
        color: #ffffff;  
        margin-top: 50px;
        margin-bottom: 20px;
        text-align:center;
    }
    
    .image-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: auto;
        ;
    }
    </style>
""", unsafe_allow_html=True)

# Título principal de la página
st.title("Anonymous NASAe 🚀")


# Imagen centrada
st.markdown('<div class="image-container">', unsafe_allow_html=True)
st.image("imagenes_web/logo.png", caption="Anonimos NASAe", width=300)
st.markdown('</div>', unsafe_allow_html=True)


#st.image("imagenes_web/logo.png",caption= "Anonimos NASAE", use_container_width=True, width=100)  # Tamaño ajustado del logo


# Espacio para "About Us"
st.markdown("<div class='about-title'>About US😎</div>", unsafe_allow_html=True)

# # Recuadro de "Sobre nosotros" en un recuadro amarillo
# col1, col2 = st.columns([1,1])

#with col1:
st.markdown("<div class='box'>We are a data consultancy made up of five members, coming from varied areas, but with the same objective and passion: improving business processes. We are specialized in providing strategic solutions based on data analysis. Our goal is to support our clients in making key decisions that drive their growth and position them as leaders in their respective industries. We work with businesses from various sectors, including restaurants and related businesses, helping them optimize their operations, identify market opportunities and improve their customer experience through the intelligent use of data.</div>", unsafe_allow_html=True)

#with col2:
