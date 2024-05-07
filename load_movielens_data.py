import pandas as pd

# Define the paths to the files
ratings_path = 'ml-100k\u.data' 
movies_path = 'ml-100k\u.item'
users_path = 'ml-100k\u.user'

# Load the data
ratings = pd.read_csv(ratings_path, sep='\t', names=['user_id', 'movie_id', 'rating', 'timestamp'], engine='python')
movies = pd.read_csv(movies_path, sep='|', encoding='ISO-8859-1', names=['movie_id', 'title', 'release_date', 'video_release_date', 'IMDb_URL', 'unknown', 'Action', 'Adventure', 'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western'], engine='python')
users = pd.read_csv(users_path, sep='|', names=['user_id', 'age', 'gender', 'occupation', 'zip_code'], engine='python')

# Check the first rows of each DataFrame
print("Ratings:")
print(ratings.head())
print("\nMovies:")
print(movies.head())
print("\nUsers:")
print(users.head())