import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix

def user_based_collaborative_filtering(filepath, user_id, num_recommendations=5):
    ratings = pd.read_csv(filepath, sep='\t', names=['user_id', 'movie_id', 'rating', 'timestamp'], engine='python')
    # Create a user-movie matrix with zeros for missing ratings
    user_movie_matrix = ratings.pivot_table(index='user_id', columns='movie_id', values='rating').fillna(0)
    # Convert the matrix to a sparse format for better efficiency
    sparse_matrix = csr_matrix(user_movie_matrix.values)
    # Calculate the cosine similarity between users
    user_similarity = cosine_similarity(sparse_matrix)
    # Create a DataFrame for user similarities
    user_similarity_df = pd.DataFrame(user_similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)
    # Get the similarities for the specific user
    similar_users = user_similarity_df[user_id].sort_values(ascending=False).iloc[1:]
    # Recommend movies based on similar users
    similar_users_ratings = user_movie_matrix.loc[similar_users.index]
    recommended_movies = (similar_users_ratings.T * similar_users).sum(axis=1) / similar_users.sum()
    recommended_movies = recommended_movies.sort_values(ascending=False).head(num_recommendations)
    return recommended_movies

# Call the function by passing the rating DataFrame, a specific user ID, and the number of recommendations
recommendations = user_based_collaborative_filtering(r'ml-100k\u.data', user_id=1)
print(recommendations)

def item_based_collaborative_filtering(filepath, movie_id, num_recommendations=5):
    ratings = pd.read_csv(filepath, sep='\t', names=['user_id', 'movie_id', 'rating', 'timestamp'], engine='python')

    # Create a movie-user matrix
    movie_user_matrix = ratings.pivot_table(index='movie_id', columns='user_id', values='rating').fillna(0)
    # Calculate the cosine similarity between movies
    movie_similarity = cosine_similarity(movie_user_matrix)
    movie_similarity_df = pd.DataFrame(movie_similarity, index=movie_user_matrix.index, columns=movie_user_matrix.index)
    # Get similar movies
    similar_movies = movie_similarity_df[movie_id].sort_values(ascending=False).iloc[1:num_recommendations+1]
    return similar_movies

# Call the function with the rating DataFrame and a movie ID
similar_movies = item_based_collaborative_filtering(r'ml-100k\u.data', movie_id=1)
print(similar_movies)