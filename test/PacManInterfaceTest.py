import unittest
import sys

# This works but I hate this
# If you can find something that works better, feel free to fix this
sys.path.append("..")
from src.PacManInterface import PacManInterface

class PacManInterfaceTest(unittest.TestCase):
	def test_get_packages(self):
		# Must make an instance of a concrete class to test this method
		pass
