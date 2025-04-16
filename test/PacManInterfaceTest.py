import unittest
import sys
import re

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
			out = pc.run_command("apt list --installed | awk -F'[ /]' '{print $1, $3}'")
			self.assertNotEqual(out, expected)
		else:
			self.assertEqual(out, expected)

	def test_get_packages(self):
		pc = PacManInterface()
		expected = re.compile(r'^(\S+\s\S+\n)*\S+\s\S+$')
		out = pc.get_packages()
		self.assertTrue(expected.match(out), "Output format does not match.")
		

def get_release():
	with open("/etc/os-release") as os_release:
		return os_release.read().lower()

if __name__ == "__main__":
	unittest.main()
