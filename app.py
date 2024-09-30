import pickle
import streamlit as st
import pandas as pd

st.title('Movie Recommender System')
movies_list = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    movie_index = movies_list[movies_list['title'].str.lower() == movie.lower()].index[0]
    distances = similarity[movie_index]
    movies_list_new = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list_new:
        movie_id = i[0]
        #fetch poster from API
        recommended_movies.append(movies_list.iloc[i[0]].title)
    return recommended_movies

selected_movie_name = st.selectbox('Choose the movie', movies_list['title'].values)
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i  in recommendations:
        st.write(i)
