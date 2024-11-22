import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer



# Load the dataset
@st.cache_data
def load_data():
    return pd.read_parquet('df_restaurants_cleaned_with_sentiment.parquet')

st.set_page_config(initial_sidebar_state="expanded")

st.markdown("""
    <style>
    .st-emotion-cache-6qob1r {
        background-color: #c9c9c9;
    }
    .plot-container{
        display:flex;
        justify-content:center;
    }
    </style>
""", unsafe_allow_html=True)

df = load_data()

st.title('Visualizador de mejora de restaurante.')

# Filter restaurants
st.sidebar.header("Selector de restaurante.")
restaurants = (
    df[df['text'].notnull() & df['business_name'].notnull()]
    .groupby('business_name')
    .filter(lambda x: len(x) > 5)['business_name']
    .unique()
)

# Select a restaurant
selected_restaurant = st.sidebar.selectbox("Seleccione o ingrese el restaurante", restaurants)

if selected_restaurant:
    st.write(f"Restaurante seleccionado: **{selected_restaurant}**")
    restaurant_data = df[df['business_name'] == selected_restaurant]
    
    # --- MÉTRICAS ---
    # Número total de reseñas
    total_reviews = restaurant_data['text'].notnull().sum()

    # Promedio de estrellas
    average_stars = restaurant_data['stars'].mean()

    # Promedio de sentimiento
    average_sentiment = restaurant_data['sentiment'].mean() * 100  # Convertir a porcentaje
    
    # Diccionario para renombrar las categorías del radar
    attribute_mapping = {
        "Cleanliness": "Limpieza",
        "Customer Service": "Atencion al Cliente",
        "Food Quality": "Calidad de la Comida",
        "Presentation": "Presentacion",
        "Wait Time": "Tiempo de Espera"
    }

    # --- GRAFICOS ---
    # Gráfico de radar para características a mejorar
    aggregated_scores = restaurant_data['scores'].apply(pd.Series).mean()
    # Personalizar nombres de las categorías
    categories = [attribute_mapping.get(attr, attr) for attr in aggregated_scores.index]
    values = list(aggregated_scores.values)
    categories += categories[:1]
    values += values[:1]

    radar_fig = px.line_polar(
        r=values,
        theta=categories,
        line_close=True,
        title="Puntos Clave a Mejorar",
        range_r=[0, max(values)]
    )
    radar_fig.update_traces(
        fill='toself',
        line_color='red',
        fillcolor='rgba(255, 0, 0, 0.3)'
    )

    # Color de la barra según el sentimiento
    bar_color = 'blue' if average_sentiment >= 0 else 'red'
    sentiment_fig = go.Figure()
    sentiment_fig.add_trace(go.Bar(
        x=['Sentimientos'],
        y=[average_sentiment],
        marker_color=bar_color,
        text=f"{average_sentiment:.2f}%",  # Mostrar el porcentaje en la barra
        textposition='outside'
    ))
    sentiment_fig.update_layout(
        title="Sentimiento Promedio",
        yaxis=dict(
            title="Nivel de sentimientos (%)",
            range=[-100, 100]  # Escala de -100% a 100%
        ),
        xaxis=dict(title=""),
        height=400,
        width=300,
        showlegend=False
    )
    
   
    # Indicador para el total de reseñas
    reviews_fig = go.Figure()
    reviews_fig.add_trace(go.Indicator(
        mode="number",
        value=total_reviews,
        title={"text": "Total de resenas"},
        number={"font": {"size": 40}},
        domain={'x': [0, 1], 'y': [0, 1]}
    ))
    reviews_fig.update_layout(
        height=200,
        width=200,
        margin=dict(t=0, b=0, l=0, r=0)
    )

    # Indicador para el promedio de estrellas
    stars_fig = go.Figure()
    stars_fig.add_trace(go.Indicator(
        mode="gauge+number",
        value=average_stars,
        title={"text": "Estrellas Promedio"},
        gauge=dict(
            axis=dict(range=[0, 5]),
            bar=dict(color="gold"),
            steps=[
                {'range': [0, 2], 'color': 'red'},
                {'range': [2, 4], 'color': 'yellow'},
                {'range': [4, 5], 'color': 'green'}
            ]
        ),
        number={"font": {"size": 40}},
        domain={'x': [0, 1], 'y': [0, 1]}
    ))
    stars_fig.update_layout(
        height=300,
        width=300,
        margin=dict(t=0, b=0, l=0, r=0)
    )

    # --- MOSTRAR GRAFICOS ---
    col1, col2 = st.columns([3, 1])
    with col1:
        st.plotly_chart(stars_fig)
        st.plotly_chart(radar_fig, use_container_width=True)
    with col2:
        st.plotly_chart(sentiment_fig, use_container_width=True)
        st.plotly_chart(reviews_fig)