import streamlit as st
import pandas as pd
import plotly.express as px
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
    </style>
""", unsafe_allow_html=True)

df = load_data()

st.title('NASAe Restaurant Business Improvement Application!')

# Filter restaurants
st.sidebar.header("Restaurant Selector")
restaurants = (
    df[df['text'].notnull() & df['business_name'].notnull()]
    .groupby('business_name')
    .filter(lambda x: len(x) > 5)['business_name']
    .unique()
)

# Select a restaurant
selected_restaurant = st.sidebar.selectbox("Select a Restaurant", restaurants)

if selected_restaurant:
    st.write(f"Selected Restaurant: **{selected_restaurant}**")
    restaurant_data = df[df['business_name'] == selected_restaurant]
    
    # Calcular promedios de las características
    aggregated_scores = restaurant_data['scores'].apply(pd.Series).mean()

    # Crear el gráfico de radar
    categories = list(aggregated_scores.index)
    values = list(aggregated_scores.values)

    # Cerrar el círculo del gráfico
    categories += categories[:1]
    values += values[:1]

    fig = px.line_polar(
        r=values,
        theta=categories,
        line_close=True,
        title="Key Areas to Improve",
        range_r=[0, max(values)]
    )
    fig.update_traces(fill='toself')

    st.plotly_chart(fig)
