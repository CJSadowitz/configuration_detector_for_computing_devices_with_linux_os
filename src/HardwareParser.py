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

	def get_CPU_info(self):
		pass

	def get_mem_info(self):
		if not self.lshw_output:
			print("ERROR: Failed to fetch memory info")
			return []
		memory = []
		for line in self.lshw_output:
			# [0] has HW path
			# [1] has class (should be memory)
			# [2:] has description
			elems = line.split()
			if elems[1] == "memory":
				desc = " ".join(elems[2:])
				memory.append(desc)
		return memory

	def get_devices(self):
		pass

	def get_linux_ver(self):
		pass
