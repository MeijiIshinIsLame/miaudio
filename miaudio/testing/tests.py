import unittest
import helpers
import os
import time

class NamesTestCase(unittest.TestCase):

	def test_convert_to_mins(self):
		result = helpers.convert_to_mins(300000)
		self.assertEqual(result, "5.00")

	def test_convert_to_milliseconds(self):
		result = helpers.convert_to_milliseconds("5:00")
		self.assertEqual(result, 300000)

if __name__ == '__main__':
	unittest.main()