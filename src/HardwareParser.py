import subprocess

class HardwareParser():
	def __init__(self):
		self.lshw_output = False
		try:
			# initialize by running the lshw command
			proc = subprocess.run([ "lshw", "-short" ], capture_output=True)
			out = proc.stdout.decode()
			# ignore table header, separator, and the last line (which is empty)
			lines = out.split("\n")[2:-1]
			self.lshw_output = lines
		except FileNotFoundError:
			print("ERROR: Could not find lshw")
		except Exception as e:
			print(f"ERROR: Unexpected error occurred when running lshw: {e}")
		self.version_read = False
		try:
			proc = subprocess.run(["cat", "/proc/version"], capture_output=True)
			self.version_read = proc.stdout.decode()
		except FileNotFoundError:
			print("ERROR: Could not find cat")
		except Exception as e:
			print(f"ERROR: Unexpected error occured when running cat: {e}")


	def get_CPU_info(self):
		return self.get_section(["processor"])

	def get_mem_info(self):
		return self.get_section(["memory"])

	def get_devices(self):
		return self.get_section(["input", "display", "bus", "network"])

	def get_linux_ver(self):
		if not self.version_read:
			print("ERROR: Failed to fetch version")
			return []
		return self.version_read

	def get_section(self, section_name_list):
		if not self.lshw_output:
			print("ERROR: Failed to fetch info")
			return []
		section = []
		for line in self.lshw_output:
			elems = line.split()
			if elems[1] in section_name_list:
				desc = " ".join(elems[2:])
				section.append(desc.strip())
			elif any(elems[1].startswith(section) for section in section_name_list):
				desc = " ".join(elems[3:])
				section.append(desc.strip())
			elif len(elems) >= 3 and elems[2] in section_name_list:
				desc = " ".join(elems[3:])
				section.append(desc.strip())

		return section
