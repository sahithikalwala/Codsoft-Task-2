class Movie:
    def __init__(self, title, genre, description):
        self.title = title
        self.genre = genre
        self.description = description

    def display(self):
        print(f"Title: {self.title}")
        print(f"Genre: {self.genre}")
        print(f"Description: {self.description}\n")


# Sample movie database
movie_db = [
    Movie("Inception", "Sci-Fi", "A mind-bending thriller about dreams within dreams."),
    Movie("The Dark Knight", "Action", "Batman faces the Joker in Gotham City."),
    Movie("Interstellar", "Sci-Fi", "A journey through space to save humanity."),
    Movie("The Notebook", "Romance", "A touching love story separated by life."),
    Movie("Avengers: Endgame", "Action", "Superheroes unite to defeat Thanos."),
    Movie("Pride and Prejudice", "Romance", "Classic love story set in the 1800s.")
]


def recommend_movies(preferred_genre):
    print(f"\nRecommendations for genre: {preferred_genre}\n")
    found = False
    for movie in movie_db:
        if preferred_genre.lower() in movie.genre.lower():
            movie.display()
            found = True

    if not found:
        print("No movies found for the selected genre.")


def main():
    print("Welcome to Simple Movie Recommendation System!")
    genre = input("Enter your preferred genre (Sci-Fi / Action / Romance): ").strip()
    recommend_movies(genre)


if __name__ == "__main__":
    main()
