from models.movie import Movie
from models.category import Category

class MovieController:
    def __init__(self):
        self.movies = []
        self.categories = []

    def create_movie(self, name, duration, description, category_names):
        categories = [self.get_or_create_category(name) for name in category_names]
        movie = Movie(name=name, duration=duration, description=description)
        movie.categories = categories
        self.movies.append(movie)

    def update_movie(self, movie, name, duration, description, category_names):
        categories = [self.get_or_create_category(name) for name in category_names]
        movie.name = name
        movie.duration = duration
        movie.description = description
        movie.categories = categories

    def delete_movie(self, movie):
        self.movies.remove(movie)

    def get_all_movies(self):
        return self.movies

    def get_or_create_category(self, name):
        for category in self.categories:
            if category.name == name:
                return category
        new_category = Category(name=name, description="")
        self.categories.append(new_category)
        return new_category