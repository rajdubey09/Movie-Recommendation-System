import pandas as pd
import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        # print(movies.iloc[i[0]].title)
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


st.title('Movie Recommender System')

# option = st.selectbox('How would you like to be contacted?', ('Email', 'Home Phone', 'Mobile Phone'))
selectedMovieName = st.selectbox('How would you like to be contacted?', movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selectedMovieName)
    for name in recommendations:
        st.write(name)
