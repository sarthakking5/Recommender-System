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
+ As not all columns were usable for our use case certain columns were selected to make the processing much faster such as:
    + Genres
    + Id
    + Keywords
    + Overview
    + Title
    + Cast
    + Crew
+ After this rows with missing values were deleted.
+ Many columns were in the form of a dictionary and to make it accessible in the form of a list a function for conversion was added.
+ After conversion the values in the data frame were now iterable and by further processing relevant names such as characters, directors, and keywords were 
  extracted.
+ Once the useful values were extracted from the columns cast, crew, keywords, and genres the items in these lists were concatenated to form a new list that was 
  saved in tags.
+ A new data frame was extracted from the present table which had only three columns id, title, and tags.

## Model Building

+ Using the PorterStemmer from NLTK library each word in the column tag was checked to see if there were multiple words with the same root word.
+ Post stemming a CountVectorizer from Sklearn was used to remove stopwords in the English language and to convert it into a vector with 5000 dimensions.
+ Cosine similarity was then used to find distances between these vectors and these distances were then sorted after applying a enumerate function that enabled to 
  preserve the original index of the vector.
+ Post this a recommend function gives us a list of 5 movies that have the closest distance to the vector of the given movie in the argument.
+  For deployment, the models were then saved in the pickle format to be further called.

## Building the Streamlit App

The main goal behind building a Streamlit app was to provide recommended similar movies to the user after they selected a certain movie along with it's poster which was fetched using the Tmdb API.

+ The recommend function in our app gave the list of five movies with the lowest cosine distance between the images.
+ Using the pickle model the value of the movie id was then fetched from the database.
+ Post fetching the id, the id was then mapped with database available of Tmdb website and the the link of the poster image was extracted from the JSON data provided by it.
+ This data was concatenated with a URL to fetch the image using the Tmdb API.
  
![](https://github.com/sarthakking5/Recommender-system/blob/main/images/result3.png)
                    Overview of the Streamlit Application Built

## Productionization

For the deployment, an open-source platform Heroku was used.

Certain files were generated for this purpose such as:
  + ProcFile
  + Setup.sh
  + .gitignore
  + requirements.txt

Now after creating a new app on the Heroku platform and connecting our GitHub repository with it, the  command `git push heroku master` leads us to the final deployed version of our app.
