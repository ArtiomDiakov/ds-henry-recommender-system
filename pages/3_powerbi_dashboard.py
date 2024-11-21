import streamlit as st

st.markdown("""
    <style>
    .st-emotion-cache-6qob1r {
        background-color: #c9c9c9;
    }
    </style>
""", unsafe_allow_html=True)

# Incrustar el iframe del dashboard
dashboard_url = "https://app.powerbi.com/view?r=eyJrIjoiYjNkNTRiZTEtNTM1Yi00NGZjLWJjYTItYjkwNDQxOWJhYjM0IiwidCI6ImZjMDA1NDdhLTI0YmItNGU0Zi05ZDYxLTczZmNhNWViOWRmMyIsImMiOjR9&pageName=73ec77b604824e04f8eb" 
iframe_code = f"""
<iframe title="GOOGLE MAPS & YELP PORJECT 001 (2)" 
    width="100%" 
    height="800px" 
    src="{dashboard_url}" 
    frameborder="0" 
    allowFullScreen="true">
</iframe>
"""
st.components.v1.html(iframe_code, height=1000, width=1000)