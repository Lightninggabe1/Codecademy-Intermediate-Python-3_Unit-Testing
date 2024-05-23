import unittest
import entertainment

class EntertainmentSystemTests(unittest.TestCase):

  def test_movie_license(self):
    daily_movies = entertainment.get_daily_movies()
    licensed_movies = entertainment.get_licensed_movies()
    for movie in daily_movies:
      print(movie)
# Write your code below:
      with self.subTest(movie):
        self.assertIn(movie, licensed_movies)

unittest.main()
