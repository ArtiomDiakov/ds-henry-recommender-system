import streamlit as st
from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split
import pandas as pd

# Cargar los datasets
@st.cache_data
def load_data():
    df = pd.read_parquet("filtered_dataset.parquet")
    df['user_id'] = df['user_id'].astype(str)
    df['business_id'] = df['business_id'].astype(str)
    return df

df = load_data()

# Preparar los datos para Surprise
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df[['user_id', 'business_id', 'stars']], reader)

# Dividir en entrenamiento y prueba
trainset, testset = train_test_split(data, test_size=0.2, random_state=42)

# Entrenar un modelo SVD
@st.cache_resource
def train_model():
    model = SVD()
    model.fit(trainset)
    return model

model = train_model()

# Función de recomendación para un usuario
def recommend_businesses_collaborative(user_id, df, model, top_n=5):
    user_businesses = df[df['user_id'] == user_id]['business_id'].unique()
    all_businesses = df['business_id'].unique()
    businesses_to_predict = [b for b in all_businesses if b not in user_businesses]
    
    # Predecir calificaciones
    predictions = [
        (business, model.predict(user_id, business).est) for business in businesses_to_predict
    ]
    
    # Ordenar por calificación predicha
    recommendations = sorted(predictions, key=lambda x: x[1], reverse=True)
    return recommendations[:top_n]

# Interfaz de usuario en Streamlit
st.title("Recomendaciones Personalizadas de Negocios")

# Selector de usuario
unique_users = df['user_id'].unique()
selected_user = st.selectbox("Selecciona un usuario (user_id):", unique_users)

# Generar recomendaciones
if st.button("Generar Recomendaciones Avanzadas"):
    recommendations = recommend_businesses_collaborative(selected_user, df, model)
    st.write("Recomendaciones para el usuario seleccionado:")
    for business_id, score in recommendations:
        business_name = df[df['business_id'] == business_id]['business_name'].iloc[0]
        st.write(f"- **{business_name}** (Predicción: {score:.2f})")
