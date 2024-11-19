import streamlit as st

# Título de la página
st.title("Dashboard de Análisis de Negocios")

st.write(
    """
    Aquí puedes visualizar el análisis interactivo desarrollado en Power BI.
    Utiliza el dashboard para explorar los datos de negocios y encontrar insights clave.
    """
)

# Incrustar el iframe del dashboard
dashboard_url = "https://app.powerbi.com/view?r=eyJrIjoiMDdhMzdkMGItZDE3Ny00MWRiLTg2NjgtYTI3N2MwMWJkZGQ0IiwidCI6ImZjMDA1NDdhLTI0YmItNGU0Zi05ZDYxLTczZmNhNWViOWRmMyIsImMiOjR9"
iframe_code = f"""
<iframe title="GOOGLE MAPS & YELP PORJECT 001 (2)" width="100%" height="600" src="{dashboard_url}" frameborder="0" allowFullScreen="true"></iframe>
"""
st.components.v1.html(iframe_code, height=650)