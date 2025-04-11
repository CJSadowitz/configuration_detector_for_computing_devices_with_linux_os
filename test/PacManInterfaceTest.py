import unittest
import sys

# This works but I hate this
# If you can find something that works better, feel free to fix this
sys.path.append("..")
from src.PacManInterface import PacManInterface

class PacManInterfaceTest(unittest.TestCase):
	# testing protections on functions
	def test_run_command_sudo(self):
		pacman = PacManInterface()
		output = pacman.run_command("sudo touch temp.txt")
		self.assertEqual(output, -1)

	def test_run_command_rm(self):
		pacman = PacManInterface()
		output = pacman.run_command("rm temp.txt")
		self.assertEqual(output, -1)

	def test_run_command_intended(self):
		pacman = PacManInterface()
		output1 = pacman.run_command("apt list --installed")
		self.assertNotEqual(output1, -1)
		output2 = pacman.run_command("pacman -Q")
		self.assertNotEqual(output2, -1)

	def test_get_packages(self):
		# Must make an instance of a concrete class to test this method
		pass

if __name__ == "__main__":
	unittest.main()
