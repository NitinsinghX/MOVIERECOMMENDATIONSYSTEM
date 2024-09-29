# setup the required modules 
import numpy as np
import pandas as pd 
import sklearn as sk
# load the data

movies= pd.read_csv("movies.csv")
ratings= pd.read_csv("ratings.csv")

print(movies.head())
print(ratings.head())

#create a user item matrix
user_movie_matrix= ratings.pivot(index="userId",columns="movieId",values="rating").fillna(0)
print(user_movie_matrix.head())

#cosine similarity
from sklearn.metrics.pairwise import cosine_similarity
similarity_matrix= cosine_similarity(user_movie_matrix)

def recommended_movies(user_Id,num_recommendations=5):
    user_index= user_Id-1
    similar_users= list(enumerate(similarity_matrix[user_index]))

    similar_users= sorted(similar_users,key=lambda x: x[1],reverse=True)[1:]


    recommended_movies= []

    for similar_user in similar_users:
        similar_user_id= similar_user[0]+1
        movies_watched= user_movie_matrix.loc[similar_user_id][user_movie_matrix.loc[similar_user_id]>0]

        for movie in movies_watched.index:
         if movie not in recommended_movies:
           recommended_movies.append(movie)
    
         if len(recommended_movies)>= num_recommendations:
           break


    return  movies[movies['movieId'].isin(recommended_movies)]["title"].tolist()

print(recommended_movies(user_Id=1))


