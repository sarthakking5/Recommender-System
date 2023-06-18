import pandas as pd
import streamlit as st
import pickle
import requests

movies_list=pickle.load(open('movies.pkl','rb'))
movies=pd.DataFrame(movies_list)
movies_list=movies_list['title'].values
similarity=pickle.load(open('similarity.pkl','rb'))

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c5ba74e8ad677b98c0912040a89179f6&language=en-US%27'.format(movie_id))
    data=response.json()
    return "http://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies_names=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].id
        recommended_movies_names.append(movies.iloc[i[0]].title)
       #fetch posters
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies_names,recommended_movies_posters



st.title('Movie Recommender System')

selected_movie_name=st.selectbox(
    'Enter Movie Title',movies['title'].values
)

if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)

    from itertools import cycle

    filteredImages = posters[0:5]
    caption = names[0:5]
    cols = cycle(st.columns(5,gap='large'))  # st.columns here since it is out of beta at the time I'm writing this
    for idx, filteredImage in enumerate(filteredImages):
        next(cols).image(filteredImage, width=150, caption=caption[idx])





# Apply custom CSS styles with the background image
import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
         
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('image3.jpg')