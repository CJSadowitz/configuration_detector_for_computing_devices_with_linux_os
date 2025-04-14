import unittest
import sys

sys.path.append("..")
from src.ReportGenerator import ReportGenerator

class ReportGeneratorTest(unittest.TestCase):
	def test_format_report_txt_get_devices(self):
		info = ["Lid Switch", "Power Button"]
		out = get_report_single(info, "txt", "get_devices")
		expected = "=== Software Installed ===\n\n\n=== CPU Info ===\n\n\n=== Memory Info ===\n\n\n=== Devices ===\nLid Switch\nPower Button\n\n=== Linux Version ===\n\n\n"
		self.assertEqual(out, expected)

	def test_format_report_txt_cpu_info(self):
		info = ["Intel(R) Celeron(R) N4120 CPU @ 1.10GHz"]
		out = get_report_single(info, "txt", "get_CPU_info")
		expected = "=== Software Installed ===\n\n\n=== CPU Info ===\nIntel(R) Celeron(R) N4120 CPU @ 1.10GHz\n\n=== Memory Info ===\n\n\n=== Devices ===\n\n\n=== Linux Version ===\n\n\n"
		self.assertEqual(out, expected)

	def test_format_report_txt_mem_info(self):
		info = ["4GiB System memory"]
		out = get_report_single(info, "txt", "get_mem_info")
		expected = "=== Software Installed ===\n\n\n=== CPU Info ===\n\n\n=== Memory Info ===\n4GiB System memory\n\n=== Devices ===\n\n\n=== Linux Version ===\n\n\n"
		self.assertEqual(out, expected)

	def test_format_report_txt_linux_ver(self):
		info = "Linux version 6.11.0-21-generic (buildd@lcy02-amd64-097) (x86_64-linux-gnu-gcc-13 (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0, GNU ld (GNU Binutils for Ubuntu) 2.42) #21~24.04.1-Ubuntu SMP PREEMPT_DYNAMIC Mon Feb 24 16:52:15 UTC 2"
		out = get_report_single(info, "txt", "get_linux_ver")
		expected = "=== Software Installed ===\n\n\n=== CPU Info ===\n\n\n=== Memory Info ===\n\n\n=== Devices ===\n\n\n=== Linux Version ===\nLinux version 6.11.0-21-generic (buildd@lcy02-amd64-097) (x86_64-linux-gnu-gcc-13 (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0, GNU ld (GNU Binutils for Ubuntu) 2.42) #21~24.04.1-Ubuntu SMP PREEMPT_DYNAMIC Mon Feb 24 16:52:15 UTC 2\n\n"
		self.assertEqual(out, expected)

	def test_format_report_txt_get_packages(self):
		info = "accountsservice 23.13.9-2ubuntu6\nacl 2.3.2-1build1.1\nadduser 3.137ubuntu1"
		out = get_report_single(info, "txt", "get_packages")
		expected = "=== Software Installed ===\naccountsservice 23.13.9-2ubuntu6\nacl 2.3.2-1build1.1\nadduser 3.137ubuntu1\n\n=== CPU Info ===\n\n\n=== Memory Info ===\n\n\n=== Devices ===\n\n\n=== Linux Version ===\n\n\n"
		self.assertEqual(out, expected)

	def test_format_report_csv_get_devices(self):
		info = ["Lid Switch", "Power Button"]
		out = get_report_single(info, "csv", "get_devices")
		expected = "Software,Version,Linux Version,CPU,Memory,Devices\n,,,,,Lid Switch,\n,,,,,Power Button,"
		self.assertEqual(out, expected)

	def test_format_report_csv_get_CPU_info(self):
		info = ["Intel(R) Celeron(R) N4120 CPU @ 1.10GHz"]
		out = get_report_single(info, "csv", "get_CPU_info")
		expected = "Software,Version,Linux Version,CPU,Memory,Devices\n,,,Intel(R) Celeron(R) N4120 CPU @ 1.10GHz,,,"
		self.assertEqual(out, expected)

	def test_format_report_csv_get_mem_info(self):
		info = ["4GiB System memory"]
		out = get_report_single(info, "csv", "get_mem_info")
		expected = "Software,Version,Linux Version,CPU,Memory,Devices\n,,,,4GiB System memory,,"
		self.assertEqual(out, expected)

	def test_format_report_csv_get_linux_ver(self):
		info = "Linux version 6.11.0-21-generic (buildd@lcy02-amd64-097) (x86_64-linux-gnu-gcc-13 (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0, GNU ld  (GNU Binutils for Ubuntu) 2.42) #21~24.04.1-Ubuntu SMP PREEMPT_DYNAMIC Mon Feb 24 16:52:15 UTC 2"
		out = get_report_single(info, "csv", "get_linux_ver")
		expected = "Software,Version,Linux Version,CPU,Memory,Devices\n,,Linux version 6.11.0-21-generic (buildd@lcy02-amd64-097) (x86_64-linux-gnu-gcc-13 (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0  GNU ld  (GNU Binutils for Ubuntu) 2.42) #21~24.04.1-Ubuntu SMP PREEMPT_DYNAMIC Mon Feb 24 16:52:15 UTC 2,,,,"
		self.assertEqual(out, expected)

	def test_format_report_csv_get_packages(self):
		info = "accountsservice 23.13.9-2ubuntu6\nacl 2.3.2-1build1.1\nadduser 3.137ubuntu1"
		out = get_report_single(info, "csv", "get_packages")
		expected = "Software,Version,Linux Version,CPU,Memory,Devices\naccountsservice,23.13.9-2ubuntu6,,,,,,\nacl,2.3.2-1build1.1\nadduser,3.137ubuntu1"
		self.assertEqual(out, expected)

	def test_format_report_json_get_devices(self):
		info = ["Lid Switch", "Power Button"]
		out = get_report_single(info, "json", "get_devices")
		expected = '{\n\t"software": [\n\t],\n\t"linux-version": "",\n\t"cpu": [\n\t],\n\t"memory": [\n\t],\n\t"devices": [\n\t\t"Lid Switch",\n\t\t"Power Button"\n\t]\n}\n'
		self.assertEqual(out, expected)

	def test_format_report_json_get_CPU_info(self):
		info = ["Intel(R) Celeron(R) N4120 CPU @ 1.10GHz"]
		out = get_report_single(info, "json", "get_CPU_info")
		expected = '{\n\t"software": [\n\t],\n\t"linux-version": "",\n\t"cpu": [\n\t\t"Intel(R) Celeron(R) N4120 CPU @ 1.10GHz"\n\t],\n\t"memory": [\n\t],\n\t"devices": [\n\t]\n}\n'
		self.assertEqual(out, expected)

	def test_format_report_json_get_mem_info(self):
		info = ["4GiB System memory"]
		out = get_report_single(info, "json", "get_mem_info")
		expected = '{\n\t"software": [\n\t],\n\t"linux-version": "",\n\t"cpu": [\n\t],\n\t"memory": [\n\t\t"4GiB System memory"\n\t],\n\t"devices": [\n\t]\n}\n'
		self.assertEqual(out, expected)

	def test_format_report_json_get_packages(self):
		info = "accountsservice 23.13.9-2ubuntu6\nacl 2.3.2-1build1.1\nadduser 3.137ubuntu1"
		out = get_report_single(info, "json", "get_packages")
		expected = '{\n\t"software": [\n\t\t{\n\t\t\t"name": "accountsservice",\n\t\t\t"version": "23.13.9-2ubuntu6"\n\t\t},\n\t\t{\n\t\t\t"name": "acl",\n\t\t\t"version": "2.3.2-1build1.1"\n\t\t},\n\t\t{\n\t\t\t"name": "adduser",\n\t\t\t"version": "3.137ubuntu1"\n\t\t}\n\t],\n\t"linux-version": "",\n\t"cpu": [\n\t],\n\t"memory": [\n\t],\n\t"devices": [\n\t]\n}\n'
		self.assertEqual(out, expected)

	def test_format_report_json_get_linux_ver(self):
		info = "Linux version 6.11.0-21-generic (buildd@lcy02-amd64-097) (x86_64-linux-gnu-gcc-13 (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0, GNU ld  (GNU Binutils for Ubuntu) 2.42) #21~24.04.1-Ubuntu SMP PREEMPT_DYNAMIC Mon Feb 24 16:52:15 UTC 2"
		out = get_report_single(info, "json", "get_linux_ver")
		expected = '{\n\t"software": [\n\t],\n\t"linux-version": "Linux version 6.11.0-21-generic (buildd@lcy02-amd64-097) (x86_64-linux-gnu-gcc-13 (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0, GNU ld  (GNU Binutils for Ubuntu) 2.42) #21~24.04.1-Ubuntu SMP PREEMPT_DYNAMIC Mon Feb 24 16:52:15 UTC 2",\n\t"cpu": [\n\t],\n\t"memory": [\n\t],\n\t"devices": [\n\t]\n}\n'
		self.assertEqual(out, expected)

	def test_format_report_txt_all(self):
		out = get_report_all("txt")
		expected = "=== Software Installed ===\naccountsservice 23.13.9-2ubuntu6\nacl 2.3.2-1build1.1\nadduser 3.137ubuntu1\n\n=== CPU Info ===\nIntel(R) Celeron(R) N4120 CPU @ 1.10GHz\n\n=== Memory Info ===\n4GiB System memory\n\n=== Devices ===\nLid Switch\nPower Button\n\n=== Linux Version ===\nLinux version 6.11.0-21-generic (buildd@lcy02-amd64-097) (x86_64-linux-gnu-gcc-13 (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0, GNU ld  (GNU Binutils for Ubuntu) 2.42) #21~24.04.1-Ubuntu SMP PREEMPT_DYNAMIC Mon Feb 24 16:52:15 UTC 2\n\n"
		self.assertEqual(out, expected)

	def test_format_report_csv_all(self):
		out = get_report_all("csv")
		expected = "Software,Version,Linux Version,CPU,Memory,Devices\naccountsservice,23.13.9-2ubuntu6,Linux version 6.11.0-21-generic (buildd@lcy02-amd64-097) (x86_64-linux-gnu-gcc-13 (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0  GNU ld  (GNU Binutils for Ubuntu) 2.42) #21~24.04.1-Ubuntu SMP PREEMPT_DYNAMIC Mon Feb 24 16:52:15 UTC 2,Intel(R) Celeron(R) N4120 CPU @ 1.10GHz,4GiB System memory,Lid Switch,\nacl,2.3.2-1build1.1,,,,Power Button,\nadduser,3.137ubuntu1"
		self.assertEqual(out, expected)

	def test_format_report_json_all(self):
		out = get_report_all("json")
		expected = ""
		self.assertEqual(out, expected)

def get_report_all(format):
	software = "accountsservice 23.13.9-2ubuntu6\nacl 2.3.2-1build1.1\nadduser 3.137ubuntu1"
	cpu = ["Intel(R) Celeron(R) N4120 CPU @ 1.10GHz"]
	mem = ["4GiB System memory"]
	devices = ["Lid Switch", "Power Button"]
	linux_ver = "Linux version 6.11.0-21-generic (buildd@lcy02-amd64-097) (x86_64-linux-gnu-gcc-13 (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0, GNU ld  (GNU Binutils for Ubuntu) 2.42) #21~24.04.1-Ubuntu SMP PREEMPT_DYNAMIC Mon Feb 24 16:52:15 UTC 2"
	rg = ReportGenerator(software, cpu, mem, devices, linux_ver)
	rg.format_report(format)
	return rg.report

def get_report_single(info, format, type):
	rg = ReportGenerator()
	match type:
		case "get_packages":
			rg.softwareInstalled = info
		case "get_CPU_info":
			rg.cpuInfo = info
		case "get_mem_info":
			rg.memInfo = info
		case "get_devices":
			rg.devicesInfo = info
		case "get_linux_ver":
			rg.linuxVer = info
	rg.format_report(format)
	return rg.report

if __name__ == "__main__":
	unittest.main()
