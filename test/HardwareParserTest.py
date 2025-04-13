import unittest
import sys

sys.path.append("..")
from src.HardwareParser import HardwareParser

class HardwareParserTest(unittest.TestCase):
	def test_get_CPU_info(self):
		pass

	def test_get_mem_info(self):
		hp = HardwareParser()

		# ovewrite output with a test case
		hp.lshw_output = [
				"/0/0                             memory         96KiB BIOS",
				"/0/200                           memory         1GiB System Memory",
				"/0/200/0                         memory         1GiB DIMM RAM Synchronous",
				"/0/1                             processor      Intel(R) Xeon(R) CPU @ 2.20GHz"
		]

		# ensure expected results match with output results
		expected = [ "96KiB BIOS", "1GiB System Memory", "1GiB DIMM RAM Synchronous" ]
		out = hp.get_mem_info()
		for e in expected:
			if e not in out or len(out) != len(expected):
				print("HardwareParser.get_mem_info() produced an unexpected result")
				print("Output was:")
				print(out)
				print("Expected:")
				print(expected)
				print("")
				return False

		# if all expected results are found, then success
		# print("HardwareParser.get_mem_info() success")
		self.assertEqual(expected, out)

	def test_get_devices(self):
		pass

	def test_get_linux_ver(self):
		pass

if __name__ == "__main__":
	unittest.main()
