# import streamlit as st

# st.title('NASAe Restaurant Buisiness Improvement Application!')

# st.write('Please Select a buisiness and it will give you 5 key points to improve you restaurant!')


import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

# Load the dataset
@st.cache
def load_data():
    return pd.read_parquet('reviews_dataset.parquet')

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
    
    # Text analysis (placeholder logic)
    def analyze_reviews(texts):
        # Example: Return scores for 5 characteristics
        return {
            "Cleanliness": 3.5,
            "Customer Service": 4.2,
            "Food Quality": 4.0,
            "Presentation": 3.8,
            "Wait Time": 3.2
        }
    
    scores = analyze_reviews(restaurant_data['text'])

    # Spider chart
    categories = list(scores.keys())
    values = list(scores.values())

    # Close the circle for radar chart
    categories += categories[:1]
    values += values[:1]

    fig = px.line_polar(
        r=values,
        theta=categories,
        line_close=True,
        title="Key Areas to Improve",
        range_r=[0, 5]
    )
    fig.update_traces(fill='toself')

    st.plotly_chart(fig)
