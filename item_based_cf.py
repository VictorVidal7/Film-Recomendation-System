import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix

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