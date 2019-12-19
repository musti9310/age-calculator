import io
from contextlib import redirect_stdout
from unittest.mock import patch
import unittest
import age_calculator
import datetime


class ContainersTestCase(unittest.TestCase):

	def setUp(self):
		self.response = io.StringIO()

	def test_check_birthdate_false(self):
		date = datetime.date.today() + datetime.timedelta(days=1)
		response = age_calculator.check_birthdate(date.year, date.month, date.day)
		self.assertFalse(response)

	def test_check_birthdate_true(self):
		response = age_calculator.check_birthdate(1990, 4, 1)
		self.assertTrue(response)

	def test_calculate_age(self):
		with redirect_stdout(self.response):
			age_calculator.calculate_age(1990, 4, 1)
			birthdate = datetime.date(1990, 4, 1)
			today = datetime.date.today()
			age = int((today-birthdate).days/365)
			self.assertTrue(str(age) in self.response.getvalue())

	def test_main_invalid(self):
		date = datetime.date.today() + datetime.timedelta(days=1)
		user_input = [date.year, date.month ,date.day]
		with redirect_stdout(self.response):
			with patch('builtins.input', side_effect=user_input):
				age_calculator.main()
				self.assertFalse("0" in self.response.getvalue())

	def test_main_valid(self):
		user_input = ['2000','1','1']
		with redirect_stdout(self.response):
			with patch('builtins.input', side_effect=user_input):
				age_calculator.main()
				birthdate = datetime.date(2000, 1, 1)
				today = datetime.date.today()
				age = int((today-birthdate).days/365)
				self.assertTrue(str(age) in self.response.getvalue())


if __name__ == '__main__':
	unittest.main()




