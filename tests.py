import unittest
import entertainment
import feedback

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

class EntertainmentSystemTests(unittest.TestCase):

  @unittest.skipIf(entertainment.regional_jet(),'Not available on regional jets')
  def test_movie_license(self):
    daily_movie = entertainment.get_daily_movie()
    licensed_movies = entertainment.get_licensed_movies()
    self.assertIn(daily_movie, licensed_movies)

  @unittest.skipUnless(entertainment.regional_jet() is False, "Not available on regional jets")
  def test_wifi_status(self):
    wifi_enabled = entertainment.get_wifi_status()
    self.assertTrue(wifi_enabled)

  def test_device_temperature(self):
    if entertainment.regional_jet():
      self.skipTest('Not available on regional jets')
    device_temp = entertainment.get_device_temp()
    self.assertLess(device_temp, 35)

  def test_maximum_display_brightness(self):
    if entertainment.regional_jet():
      self.skipTest('Not available on regional jets')
    brightness = entertainment.get_maximum_display_brightness()
    self.assertAlmostEqual(brightness, 400)


unittest.main()



class CustomerFeedbackTests(unittest.TestCase):

  # Write your code below:
  @unittest.expectedFailure
  def test_survey_form(self):
    self.assertEqual(feedback.issue_survey(), 'Success')

  def test_complaint_form(self):
    self.assertEqual(feedback.log_customer_complaint(), 'Success')

unittest.main()
