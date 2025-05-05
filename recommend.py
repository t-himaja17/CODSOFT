import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Load the data
movies = pd.read_csv('movies.csv')

# Step 2: Convert genres into numbers (TF-IDF)
vectorizer = TfidfVectorizer()
genre_matrix = vectorizer.fit_transform(movies['genre'])

# Step 3: Calculate similarity
similarity = cosine_similarity(genre_matrix)

# Step 4: Recommendation function
def recommend(movie_title):
    if movie_title not in movies['title'].values:
        print("Movie not found in database.")
        return

    idx = movies[movies['title'] == movie_title].index[0]
    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]  # Top 3 similar movies

    print(f"\nBecause you liked '{movie_title}', you may also like:")
    for i, score in sim_scores:
        print(f"- {movies.iloc[i]['title']}")

# Step 5: Try it
movie = input("Enter a movie title: ")
recommend(movie)
