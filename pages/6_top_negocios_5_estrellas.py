import pandas as pd
import streamlit as st

# Cargar los datasets
df = pd.read_parquet("filtered_dataset.parquet")

# Calcular las estadísticas por negocio
business_avg_stars = df.groupby('business_id').agg(
    avg_stars=('stars', 'mean'),
    total_reviews=('review_id', 'count'),
    business_name=('business_name', 'first')  # Agregamos el nombre del negocio
).reset_index()

# Función para recomendar negocios
def recommend_businesses(user_id, df, business_df, top_n=5):
    # Obtener los negocios ya visitados por el usuario
    user_businesses = df[df['user_id'] == user_id]['business_id'].unique()
    # Filtrar negocios no visitados
    recommendations = business_df[~business_df['business_id'].isin(user_businesses)]
    # Ordenar por calificación promedio y número total de reseñas
    recommendations = recommendations.sort_values(
        by=['avg_stars', 'total_reviews'], ascending=[False, False]
    )
    return recommendations.head(top_n)

# Interfaz Streamlit
st.title("Recomendación de Negocios")
st.write("Seleccione un usuario para obtener recomendaciones de negocios.")

# Lista de user_id únicos
unique_users = df['user_id'].unique()

# Selector de usuario
selected_user = st.selectbox("Selecciona un user_id:", unique_users)

# Mostrar recomendaciones al usuario seleccionado
if st.button("Generar Recomendaciones"):
    recommendations = recommend_businesses(selected_user, df, business_avg_stars)
    
    st.write("Recomendaciones para el usuario seleccionado:")
    # Mostrar tabla con el nombre del negocio incluido
    st.table(recommendations[['business_name', 'business_id', 'avg_stars', 'total_reviews']])
