import unittest
from controllers.movie_controller import MovieController

class TestMovieController(unittest.TestCase):
    def setUp(self):
        self.movie_controller = MovieController()

    def test_create_movie(self):
        self.movie_controller.create_movie("Inception", 148, "A mind-bending thriller", ["Action", "Sci-Fi"])
        movies = self.movie_controller.get_all_movies()
        self.assertEqual(len(movies), 1)
        self.assertEqual(movies[0].name, "Inception")

    def test_update_movie(self):
        self.movie_controller.create_movie("Inception", 148, "A mind-bending thriller", ["Action", "Sci-Fi"])
        movie = self.movie_controller.get_all_movies()[0]
        self.movie_controller.update_movie(movie, "Inception", 148, "Updated description", ["Action", "Thriller"])
        updated_movie = self.movie_controller.get_all_movies()[0]
        self.assertEqual(updated_movie.description, "Updated description")
        self.assertIn("Thriller", [category.name for category in updated_movie.categories])

    def test_delete_movie(self):
        self.movie_controller.create_movie("Inception", 148, "A mind-bending thriller", ["Action", "Sci-Fi"])
        movie = self.movie_controller.get_all_movies()[0]
        self.movie_controller.delete_movie(movie)
        movies = self.movie_controller.get_all_movies()
        self.assertEqual(len(movies), 0)

    def test_get_or_create_category(self):
        category = self.movie_controller.get_or_create_category("Action")
        self.assertEqual(category.name, "Action")
        category_duplicate = self.movie_controller.get_or_create_category("Action")
        self.assertEqual(category, category_duplicate)

if __name__ == "__main__":
    unittest.main()