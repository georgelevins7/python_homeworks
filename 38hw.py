from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Movies",
    version="1.0.0"
)

movies = [
    {"id": 1, "title": "Inception", "genre": "Sci-Fi", "year": 2010, "rating": 8.8},
    {"id": 2, "title": "The Matrix", "genre": "Sci-Fi", "year": 1999, "rating": 8.7},
    {"id": 3, "title": "Interstellar", "genre": "Sci-Fi", "year": 2014, "rating": 8.6},
    {"id": 4, "title": "The Dark Knight", "genre": "Action", "year": 2008, "rating": 9.0},
    {"id": 5, "title": "Pulp Fiction", "genre": "Crime", "year": 1994, "rating": 8.9},
    {"id": 6, "title": "Fight Club", "genre": "Drama", "year": 1999, "rating": 8.8},
    {"id": 7, "title": "Forrest Gump", "genre": "Drama", "year": 1994, "rating": 8.8},
    {"id": 8, "title": "The Lord of the Rings: The Return of the King", "genre": "Fantasy", "year": 2003, "rating": 8.9},
    {"id": 9, "title": "The Godfather", "genre": "Crime", "year": 1972, "rating": 9.2},
    {"id": 10, "title": "The Shawshank Redemption", "genre": "Drama", "year": 1994, "rating": 9.3}
]


@app.get("/movies/{movie_id}")
def read_movie(movie_id: int):
    filtered_movies = [movie for movie in movies if movie["id"] == movie_id]
    if not filtered_movies:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"movie": filtered_movies[0]}

@app.get("/movies")
def read_movies(
    genre: str | None = None,
    year: int | None = None,
    min_rating: float | None = None,
    search: str | None = None):
    filtered_movies = movies
    if genre is not None:
        filtered_movies = [movie for movie in filtered_movies if movie["genre"].lower() == genre.lower()]
    if year is not None:
        filtered_movies = [movie for movie in filtered_movies if movie["year"] == year]
    if min_rating is not None:
        filtered_movies = [movie for movie in filtered_movies if movie["rating"] >= min_rating]
    if search is not None:
        filtered_movies = [movie for movie in filtered_movies if search.lower() in movie["title"].lower()]
    return {"movies": filtered_movies}
