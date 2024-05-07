import pandas as pd

def load_and_explore():
    # Define the paths to the files
    ratings_path = r'ml-100k\u.data' 
    movies_path = r'ml-100k\u.item'
    users_path = r'ml-100k\u.user'

    # Load the data
    ratings = pd.read_csv(ratings_path, sep='\t', names=['user_id', 'movie_id', 'rating', 'timestamp'], engine='python')
    movies = pd.read_csv(movies_path, sep='|', encoding='ISO-8859-1', names=['movie_id', 'title', 'release_date', 'video_release_date', 'IMDb_URL', 'unknown', 'Action', 'Adventure', 'Animation', "Children's", 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western'], engine='python')
    users = pd.read_csv(users_path, sep='|', names=['user_id', 'age', 'gender', 'occupation', 'zip_code'], engine='python')

    # Explore the ratings data
    print("Ratings Data:")
    print(ratings.head())
    print(ratings.describe())
    print(ratings.info())

    # Explore the movies data
    print("\nMovies Data:")
    print(movies.head())
    print(movies.describe(include='all'))
    print(movies.info())

    # Analyze the distribution of genres
    genre_columns = ['Action', 'Adventure', 'Animation', "Children's", 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
    for genre in genre_columns:
        print(f"\nDistribution of {genre} Movies:")
        print(movies[genre].value_counts())

    # Explore the users data
    print("\nUsers Data:")
    print(users.head())
    print(users.describe())
    print(users.info())

    # Distribution of user occupations
    print("\nDistribution of User Occupations:")
    print(users['occupation'].value_counts())

if __name__ == "__main__":
    load_and_explore()