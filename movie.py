import streamlit as st
import pandas as pd
import pickle
import requests
import zipfile



zip_file_path = 'similarity.pkl.zip'
pickle_file_name = 'similarity.pkl'
with zipfile.ZipFile(zip_file_path, 'r') as z:
    with z.open(pickle_file_name) as f:
        sim = pickle.load(f)
movies=pickle.load(open('movie_list.pkl','rb'))
movie=movies['original_title'].values

def poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=31f54178adaedd86d54fef8d84a0684e&language=en-US'.format(movie_id))
    data=response.json()
    poster_path=data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommed(movie):
    idx=movies[movies['original_title']==movie].index[0]
    #st.write(movies['movie_id']==movie)
    distances=sorted(list(enumerate(sim[idx])),reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    col1, col2, col3,col4,col5 = st.columns(5)
    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].original_title)
        recommended_movie_posters.append(poster(movies.iloc[i[0]].movie_id))
    return recommended_movie_names,recommended_movie_posters

option = st.selectbox(
    "Select your intersted movie",
    (movie),
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters=recommed(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.write(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.write(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.write(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.write(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.write(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])