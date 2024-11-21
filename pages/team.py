import streamlit as st
import base64

st.set_page_config(layout='wide')

st.markdown(
    """
    <style>
        .st-emotion-cache-6qob1r {
        background-color: #c9c9c9;
    }
        about-us{
            margin:auto;
            text-align:center;
        }
        div[data-testid="stColumn"]
        {  
            text-align: center;
            align-items: center;
            margin: auto;
            
            .logo-container{
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 10px;
            border: 1px solid red;
            }
            .logo{
                display:flex;
                border: 1px solid red;
            }
            [data-testid="stFullScreenFrame"]{
                display:flex;
                justify-content:center;
                max-width:300px;
            }
            div[data-testid="stImageCaption"]{
                font-size: 24px;
            }
        }
    </style>
    """,unsafe_allow_html=True
)

st.title("About Us")

col1, col2, col3,col4,col5 = st.columns(5)

with col1:
    # Imagen centrada con st.image
    st.markdown('<div class="centered">', unsafe_allow_html=True)
    st.image("imagenes_web/agostina.png", use_container_width=True, caption="Agostina")
    st.markdown('</div>', unsafe_allow_html=True)


    
    st.markdown(
    """<a href="https://www.linkedin.com/in/agostina-fernández-aab4a8323/">
    <img src="data:image/png;base64,{}" width="50">
    </a>""".format(
        base64.b64encode(open("imagenes_web/linkedin_logo.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
    
    st.markdown(
    """<a href="https://github.com/DataSciGina">
    <img src="data:image/png;base64,{}" width="50">
    </a>""".format(
        base64.b64encode(open("imagenes_web/github_logo.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)

with col2:
    # Imagen centrada con st.image
    st.markdown('<div class="centered">', unsafe_allow_html=True)
    st.image("imagenes_web/artem.png", caption="Artiom")
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown(
    """<a href="https://www.linkedin.com/in/artiom-diakov/">
    <img src="data:image/png;base64,{}" width="50">
    </a>""".format(
        base64.b64encode(open("imagenes_web/linkedin_logo.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
    
    st.markdown(
    """<a href="https://github.com/ArtiomDiakov">
    <img src="data:image/png;base64,{}" width="50">
    </a>""".format(
        base64.b64encode(open("imagenes_web/github_logo.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
with col3:
    # Imagen centrada con st.image
    st.markdown('<div class="centered">', unsafe_allow_html=True)
    st.image("imagenes_web/esteban.png", caption= "Esteban")
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown(
    """<a href="https://www.linkedin.com/in/andrés-esteban-gutierrez-nivia-9035a62b7/">
    <img src="data:image/png;base64,{}" width="50">
    </a>""".format(
        base64.b64encode(open("imagenes_web/linkedin_logo.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
    
    st.markdown(
    """<a href="https://github.com/aestebangnivia23">
    <img src="data:image/png;base64,{}" width="50">
    </a>""".format(
        base64.b64encode(open("imagenes_web/github_logo.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
with col4:
    # Imagen centrada con st.image
    st.markdown('<div class="centered">', unsafe_allow_html=True)
    st.image("imagenes_web/nico.png", caption="Nicolas")
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown(
    """<a href="https://www.linkedin.com/in/nicolas-aballay-6a3543335/">
    <img src="data:image/png;base64,{}" width="50">
    </a>""".format(
        base64.b64encode(open("imagenes_web/linkedin_logo.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
    
    st.markdown(
    """<a href="https://github.com/AballayNicolas">
    <img src="data:image/png;base64,{}" width="50">
    </a>""".format(
        base64.b64encode(open("imagenes_web/github_logo.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
with col5:
    # Imagen centrada con st.image
    st.markdown('<div class="centered">', unsafe_allow_html=True)
    st.image("imagenes_web/santino.png", caption="Santino")
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown(
    """<a href="https://www.linkedin.com/in/santino-martín-rocchietti-7aa0b7318/">
    <img src="data:image/png;base64,{}" width="50">
    </a>""".format(
        base64.b64encode(open("imagenes_web/linkedin_logo.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
    
    st.markdown(
    """<a href="https://github.com/Santino-Rocchietti">
    <img src="data:image/png;base64,{}" width="50">
    </a>""".format(
        base64.b64encode(open("imagenes_web/github_logo.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
    