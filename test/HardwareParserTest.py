import unittest
import sys

sys.path.append("..")
from src.HardwareParser import HardwareParser

class HardwareParserTest(unittest.TestCase):
	def test_get_devices(self):
		hp = HardwareParser()

		hp.lshw_output = [
				"/0/100/1f.1              bus            Celeron/Pentium Silver Processor Gaussian Mixture Model",
				"/1             input0    input          Lid Switch",
				"/2             input1    input          Power Button",
				"/0/100/14/0    eno1      network        RTL8111/8168/8211/8411 PCI Express Gigabit Ethernet Controller",
				"/0/100/2       /dev/fb0  display        GeminiLake [UHD Graphics 600]",
				"/0/0                     memory         4GiB System memory",
				"/0/1                     processor      Intel(R) Celeron(R) N4120 CPU @ 1.10GHz"
		]
		expected = [
				"Celeron/Pentium Silver Processor Gaussian Mixture Model",
				"Lid Switch",
				"Power Button",
				"RTL8111/8168/8211/8411 PCI Express Gigabit Ethernet Controller",
				"GeminiLake [UHD Graphics 600]"
		]
		out = hp.get_devices()
		self.assertEqual(expected, out)
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

	def test_get_CPU_info(self):
		hp = HardwareParser()
		hp.lshw_output = [
				"/0                       bus            Motherboard",
				"/0/0                     memory         4GiB System memory",
				"/0/1                     processor      Intel(R) Celeron(R) N4120 CPU @ 1.10GHz"
		]
		expected = ["Intel(R) Celeron(R) N4120 CPU @ 1.10GHz"]
		out = hp.get_CPU_info()
		self.assertEqual(expected, out)

	def test_get_linux_ver(self):
		pass

if __name__ == "__main__":
	unittest.main()
