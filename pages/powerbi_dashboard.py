import streamlit as st

# Incrustar el iframe del dashboard
dashboard_url = "https://app.powerbi.com/view?r=eyJrIjoiMDdhMzdkMGItZDE3Ny00MWRiLTg2NjgtYTI3N2MwMWJkZGQ0IiwidCI6ImZjMDA1NDdhLTI0YmItNGU0Zi05ZDYxLTczZmNhNWViOWRmMyIsImMiOjR9&pageName=73ec77b604824e04f8eb"
iframe_code = f"""
<iframe title="GOOGLE MAPS & YELP PORJECT 001 (2)" 
    width="100%" 
    height="600" 
    src="{dashboard_url}" 
    frameborder="0" 
    allowFullScreen="true">
</iframe>
"""
st.components.v1.html(iframe_code, height=800)