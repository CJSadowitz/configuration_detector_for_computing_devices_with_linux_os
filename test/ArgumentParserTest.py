import unittest
import sys

sys.path.append("..")
from src.ArgumentParser import ArgumentParser

class ArgumentParserTest(unittest.TestCase):
	def test_get_cmd_arguments_get_packages(self):
		test_args = ['n/a', '--get_packages']
		sys.argv = test_args

		argument_parser_obj = ArgumentParser()
		args = argument_parser_obj.get_cmd_arguments()

		self.assertTrue(args.get_packages)
		self.assertFalse(args.get_CPU_info)
		self.assertFalse(args.get_mem_info)
		self.assertFalse(args.get_devices)
		self.assertFalse(args.get_linux_ver)

if __name__ == "__main__":
	unittest.main()
