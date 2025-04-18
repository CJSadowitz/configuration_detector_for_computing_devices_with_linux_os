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
		try:
			if get_release() == "arch":
				out = pc.run_command("pacman -Q")
				self.assertNotEqual(out, expected)
			else:
				self.assertEqual(out, expected)
		except Exception as e:
			self.assertEqual(out, expected)

	def test_run_command_ubuntu(self):
		pc = PacManInterface()
		expected, out = [], []
		try:
			if get_release() == "ubuntu":
				out = pc.run_command("apt list --installed | awk -F'[ /]' '{print $1, $3}'")
				self.assertNotEqual(out, expected)
			else:
				self.assertEqual(out, expected)
		except Exception as e:
			self.assertEqual(out, expected)

	def test_get_packages(self):
		pc = PacManInterface()
		expected = re.compile(r'^(\S+\s\S+\n)*\S+\s\S+$')
		# This depends on the user testing this code to be on a linux os
		out = pc.get_packages()
		if out != "OS not identifiable.":
			out_lines = out.split('\n')
			for line in out_lines:
				does_match = re.match(r'^\S+\s\S+$', line)
				if not does_match:
					self.assertTrue(False, line)
		if (out == "OS not identifiable."):
			# Example output for non windows systems
			out = "xkb-data 2.41-2ubuntu1.1\nxml-core 0.19\nxorg-docs-core 1:1.7.1-1.2\nxorg-sgml-doctools 1:1.11-1.1\nxorg 1:7.7+23ubuntu3"
		result = expected.match(out)
		if result == None: # Strings do not match; out does not follow the regex
			result = False
		self.assertTrue(result, "Output format does not match.")

def get_release():
	with open("/etc/os-release") as os_release:
		return os_release.read().lower()

if __name__ == "__main__":
	unittest.main()
