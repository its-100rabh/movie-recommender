import streamlit as st
import pickle
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch the API key from environment
api_key = os.getenv('apiKey')

# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:10]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Load movie data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit UI
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select your Movie',
    movies['title'].values)

if st.button('Recommend'):
    st.write('Movie Chosen : ', selected_movie_name)
    for i in recommend(selected_movie_name):
        st.write('Movie Recommended : ', i)

# Setting the custom port (if you want to specify a port explicitly)
if __name__ == '__main__':
    # Streamlit takes care of this under the hood, but you can run it with custom parameters if necessary.
    # For instance, setting the port for local development:
    os.system('streamlit run app.py --server.port=8502')  # You can change 8502 to any port you'd prefer
