# Movie Recommender System: Project Overview

+ Developed a tool that recommends movies to its users when to help them in watching similar movies.

+ Used TMDB dataset containing data of 5000 movies and processed it using python.

+ Engineered features from the text using NLTK to remove stopwords and vectorize the characteristics of each movie such as cast, director, genres, and taglines.

+ Found the distance of each vector from one other in the 5000-dimensional space.

+ Built an interactive app using Streamlit to display recommendations.

+ Displayed the images tags of each movie after fetching data from Tmdb API.
  
![](https://github.com/sarthakking5/Recommender-system/blob/main/images/resultf.gif)

## Code and Resources Used

**Python Version**: 3.11 **Packages Used**: Pandas, Numpy, ast, NLTK, Sklearn, Streamlit, Requests, Pickle\
**App Framework Requirements**: `pip install -r requirements.txt`\
**Dataset**: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv \
**Tmdb API**: https://developer.themoviedb.org/reference/intro/getting-started

## Data Cleaning and Processing

For our data to be made more usable certain changes were made to it.

+ Both datasets were merged on the common column 'title'.
+ As not all columns were usable for our use-case certain columns were selected to make the processing much faster such as:
    + Genres
    + Id
    + Keywords
    + Overview
    + Title
    + Cast
    + Crew
+ After this rows with missing values were deleted.
+ Many columns were in the form of a dictionary and to make it accessible in the form of a list a function for conversion was added.
+ After conversion the values in the data frame were now iterable and bu further processing relevant names such as characters, directors, and keywords were 
  extracted.
+
+ 
