import unittest
import sys

sys.path.append("..")
from src.ArgumentParser import ArgumentParser

class ArgumentParserTest(unittest.TestCase):
	# Test individual arguments to show the syntax for each and that they individually work
	def test_get_packages(self):
		test_args = ['n/a', '--get_packages']
		sys.argv = test_args

		argument_parser_obj = ArgumentParser()
		args = argument_parser_obj.get_cmd_arguments()

		self.assertTrue(args.get_packages)
		self.assertFalse(args.get_CPU_info)
		self.assertFalse(args.get_mem_info)
		self.assertFalse(args.get_devices)
		self.assertFalse(args.get_linux_ver)

	def test_get_CPU_info(self):
		test_args = ['n/a', '--get_CPU_info']
		sys.argv = test_args

		argument_parser_obj = ArgumentParser()
		args = argument_parser_obj.get_cmd_arguments()

		self.assertFalse(args.get_packages)
		self.assertTrue(args.get_CPU_info)
		self.assertFalse(args.get_mem_info)
		self.assertFalse(args.get_devices)
		self.assertFalse(args.get_linux_ver)

	def test_get_mem_info(self):
		test_args = ['n/a', '--get_mem_info']
		sys.argv = test_args

		argument_parser_obj = ArgumentParser()
		args = argument_parser_obj.get_cmd_arguments()

		self.assertFalse(args.get_packages)
		self.assertFalse(args.get_CPU_info)
		self.assertTrue(args.get_mem_info)
		self.assertFalse(args.get_devices)
		self.assertFalse(args.get_linux_ver)

	def test_get_devices(self):
		test_args = ['n/a', '--get_devices']
		sys.argv = test_args

		argument_parser_obj = ArgumentParser()
		args = argument_parser_obj.get_cmd_arguments()

		self.assertFalse(args.get_packages)
		self.assertFalse(args.get_CPU_info)
		self.assertFalse(args.get_mem_info)
		self.assertTrue(args.get_devices)
		self.assertFalse(args.get_linux_ver)

	def test_get_linux_ver(self):
		test_args = ['n/a', '--get_linux_ver']
		sys.argv = test_args

		argument_parser_obj = ArgumentParser()
		args = argument_parser_obj.get_cmd_arguments()

		self.assertFalse(args.get_packages)
		self.assertFalse(args.get_CPU_info)
		self.assertFalse(args.get_mem_info)
		self.assertFalse(args.get_devices)
		self.assertTrue(args.get_linux_ver)

	# Show that any can be used at a time
	def test_all(self):
		test_args = ['n/a', '--get_packages', '--get_CPU_info', '--get_mem_info', '--get_devices', '--get_linux_ver']
		sys.argv = test_args

		argument_parser_obj = ArgumentParser()
		args = argument_parser_obj.get_cmd_arguments()

		self.assertTrue(args.get_packages)
		self.assertTrue(args.get_CPU_info)
		self.assertTrue(args.get_mem_info)
		self.assertTrue(args.get_devices)
		self.assertTrue(args.get_linux_ver)

	# Show that order does not matter
	def test_all_inverse_order(self):
		test_args = ['n/a', '--get_linux_ver', '--get_devices', '--get_mem_info', '--get_CPU_info', '--get_packages']
		sys.argv = test_args

		argument_parser_obj = ArgumentParser()
		args = argument_parser_obj.get_cmd_arguments()

		self.assertTrue(args.get_packages)
		self.assertTrue(args.get_CPU_info)
		self.assertTrue(args.get_mem_info)
		self.assertTrue(args.get_devices)
		self.assertTrue(args.get_linux_ver)

	# Show that function will return -1 error code for bad argument
	def test_wrong_arg(self):
		# Typo in an argument
		test_args = ['n/a', '--get_', '--get_packages']
		sys.argv = test_args

		argument_parser_obj = ArgumentParser()
		args = argument_parser_obj.get_cmd_arguments()

		self.assertEqual(args, -1)
if __name__ == "__main__":
	unittest.main()

