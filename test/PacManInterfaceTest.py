import unittest
import sys

sys.path.append("..")
from src.PacManInterface import PacManInterface

class PacManInterfaceTest(unittest.TestCase):
	def test_run_command_rm(self):
		pc = PacManInterface()
		out = pc.run_command("rm")
		expected = []
		self.assertEqual(out, expected)

	def test_run_command_pacman(self):
		pc = PacManInterface()
		expected, out = [], []
		if get_release() == "arch":
			out = pc.run_command("pacman -Q")
			self.assertNotEqual(out, expected)
		else:
			self.assertEqual(out, expected)

	def test_run_command_pacman(self):
		pc = PacManInterface()
		expected, out = [], []
		if get_release() == "ubuntu":
			out = pc.run_command("apt list --installed")
			self.assertNotEqual(out, expected)
		else:
			self.assertEqual(out, expected)

	def test_get_packages(self):
		# Some minor changes to code may need to be done to unit test
		# or use some funny functions that are a part of python unittest
		pass

def get_release():
	with open("/etc/os-release") as os_release:
		return os_release.read().lower()

if __name__ == "__main__":
	unittest.main()
