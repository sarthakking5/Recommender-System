#!/usr/bin/env python
# coding: utf-8

# In[338]:


import pandas as pd





movies=pd.read_csv('tmdb_5000_movies.csv')





movies.head(2)





credits=pd.read_csv('tmdb_5000_credits.csv')





credits.head(3)




movies=pd.merge(movies,credits,on='title')





movies.columns





#selecting the columns
#genres
#id
#keywords
#overview
#title
#cast
#crew
movies=movies[['genres','id','keywords','title','overview','cast','crew']]





movies.head(2)


#


movies.shape





movies.isnull().sum()


#


#dropping null values
movies.dropna(inplace=True)





import ast





#function for conversion
counter=0
def convert(obj):
    global counter
    l=[]
    for i in obj:
        l.append(i['name'])
    counter+=1
    return l


:


#converting genres
movies['genres']=movies.genres.apply(lambda x: convert(ast.literal_eval(x)))





#converting keywords
movies['keywords']=movies.keywords.apply(lambda x: convert(ast.literal_eval(x)))




#converting top3 values if cast
def convert3(obj):
    counter=0
    l=[]
    for i in obj:
        if counter!=3:
            l.append(i['name'])
            counter+=1
        else:
            break
    return l





movies['cast']=movies.cast.apply(lambda x: convert3(ast.literal_eval(x)))





#function for fetching director name
def f_dr(obj):
    l=[]
    for i in obj:
        if i['job']=='Director':
            l.append(i['name'])
    return l
            





#fetching director name 
movies['crew']=movies.crew.apply(lambda x: f_dr(ast.literal_eval(x)))





movies['overview']=movies.overview.apply(lambda x : x.split(" "))





movies['genres']=movies.genres.apply(lambda x : [i.replace(' ','') for i in x])





movies['cast']=movies.cast.apply(lambda x : [i.replace(' ','') for i in x])
movies['keywords']=movies.keywords.apply(lambda x : [i.replace(' ','') for i in x])




movies['crew']=movies.crew.apply(lambda x : [i.replace(' ','') for i in x])





movies['tags']=movies['overview']+movies['keywords']+movies['cast']+movies['crew']





movies.head()





new_df=movies[['id','title','tags']]


:


new_df['tags']=new_df.tags.apply(lambda x:" ".join(x))





new_df['tags']=new_df.tags.apply(lambda x:x.lower())




new_df['tags'][0]




new_df['tags']=new_df.tags.apply(lambda x:stem(x))





new_df.head()





import nltk




from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()





def stem(text):
    y=[]
    for i in text.split():
        y.append(ps.stem(i))
    
    return " ".join(y)


]:


from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=5000,stop_words='english')





vectors=cv.fit_transform(new_df['tags']).toarray()


:


vectors[0]





cv.get_feature_names_out()




from sklearn.metrics.pairwise import cosine_similarity





similarity=cosine_similarity(vectors)





sorted(list(enumerate(similarity[0])),reverse=True,key=lambda x:x[1])[1:6]




def recommend(movie):
    movie_index=new_df[new_df['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    for i in movies_list:
        print(new_df.iloc[i[0]].title)
    





recommend('Batman')





new_df.iloc[1216].title





import pickle





pickle.dump(new_df,open('movies.pkl','wb'))





pickle.dump(similarity,open('similarity.pkl','wb'))






