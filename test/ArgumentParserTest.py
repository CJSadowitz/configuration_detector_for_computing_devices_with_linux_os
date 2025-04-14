import unittest
import sys

sys.path.append("..")
from src.ArgumentParser import ArgumentParser

class ArgumentParserTest(unittest.TestCase):
	# Test individual arguments to show the syntax for each and that they individually work
	def test_get_packages(self):
		args = get_args(['n/a', '--get_packages', '--file_type', 'txt'])

		self.assertTrue(args.get_packages)
		self.assertFalse(args.get_CPU_info)
		self.assertFalse(args.get_mem_info)
		self.assertFalse(args.get_devices)
		self.assertFalse(args.get_linux_ver)

	def test_get_CPU_info(self):
		args = get_args(['n/a', '--get_CPU_info', '--file_type', 'txt'])

		self.assertFalse(args.get_packages)
		self.assertTrue(args.get_CPU_info)
		self.assertFalse(args.get_mem_info)
		self.assertFalse(args.get_devices)
		self.assertFalse(args.get_linux_ver)

	def test_get_mem_info(self):
		args = get_args(['n/a', '--get_mem_info', '--file_type', 'txt'])

		self.assertFalse(args.get_packages)
		self.assertFalse(args.get_CPU_info)
		self.assertTrue(args.get_mem_info)
		self.assertFalse(args.get_devices)
		self.assertFalse(args.get_linux_ver)

	def test_get_devices(self):
		args = get_args(['n/a', '--get_devices', '--file_type', 'txt'])

		self.assertFalse(args.get_packages)
		self.assertFalse(args.get_CPU_info)
		self.assertFalse(args.get_mem_info)
		self.assertTrue(args.get_devices)
		self.assertFalse(args.get_linux_ver)

	def test_get_linux_ver(self):
		args = get_args(['n/a', '--get_linux_ver', '--file_type', 'txt'])

		self.assertFalse(args.get_packages)
		self.assertFalse(args.get_CPU_info)
		self.assertFalse(args.get_mem_info)
		self.assertFalse(args.get_devices)
		self.assertTrue(args.get_linux_ver)

	# Show that any can be used at a time
	def test_all(self):
		args = get_args(['n/a', '--file_type', 'txt', '--get_packages', '--get_CPU_info', '--get_mem_info', '--get_devices', '--get_linux_ver'])

		self.assertTrue(args.get_packages)
		self.assertTrue(args.get_CPU_info)
		self.assertTrue(args.get_mem_info)
		self.assertTrue(args.get_devices)
		self.assertTrue(args.get_linux_ver)

	# Show that order does not matter
	def test_all_inverse_order(self):
		args = get_args(['n/a', '--file_type', 'txt', '--get_linux_ver', '--get_devices', '--get_mem_info', '--get_CPU_info', '--get_packages'])

		self.assertTrue(args.get_packages)
		self.assertTrue(args.get_CPU_info)
		self.assertTrue(args.get_mem_info)
		self.assertTrue(args.get_devices)
		self.assertTrue(args.get_linux_ver)

	def test_wrong_arg(self):
		args = get_args(['n/a', '--get_', '--get_packages'])

		self.assertEqual(args, -1)

	def test_action_arg_wrong_choice(self):
		args = get_args(['n/a', '--action', 'n'])

		result = None
		try:
			result = args.action
		except Exception as e:
			pass

		self.assertNotEqual(result, 's')
		self.assertNotEqual(result, 'p')
		self.assertEqual(result, None)

	def test_file_type_wrong_choice(self):
		args = get_args(['n/a', '--file_type', 'obj'])

		result = None
		try:
			result = args.file_type
		except Exception as e:
			pass

		self.assertNotEqual(result, "csv")
		self.assertNotEqual(result, "txt")
		self.assertNotEqual(result, "json")
		self.assertEqual(result, None)

	def test_file_type_correct_choice(self):
		args = get_args(['n/a', '--file_type', 'csv'])

		result = None
		try:
			result = args.file_type
		except Exception as e:
			pass

		self.assertEqual(result, "csv")
		self.assertNotEqual(result, "txt")
		self.assertNotEqual(result, "json")

	def test_action_correct_choice(self):
		args = get_args(['n/a', '--action', 's', '--file_type', 'txt'])

		result = None
		try:
			result = args.action
		except Exception as e:
			pass

		self.assertEqual(result, "s")
		self.assertNotEqual(result, "p")


def get_args(arg_list):
	sys.argv = arg_list
	argument_parser_obj = ArgumentParser()
	return argument_parser_obj.get_cmd_arguments()

if __name__ == "__main__":
	unittest.main()

