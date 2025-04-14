import argparse

class ArgumentParser():
	def __init__(self):
		# Setup all arguments
		parser = argparse.ArgumentParser(description="A command line tool that shows the user the configuration details of the system")
		parser.add_argument("--get_packages", action="store_true", help="returns a list of all installed software")
		parser.add_argument("--get_CPU_info", action="store_true", help="returns CPU info")
		parser.add_argument("--get_mem_info", action="store_true", help="returns information on memory")
		parser.add_argument("--get_devices",  action="store_true", help="returns a list of connected peripherals")
		parser.add_argument("--get_linux_ver",  action="store_true", help="returns linux version")
		parser.add_argument("--file_type", type=str, choices=["csv", "txt", "json"], required=True, help="save file type")
		parser.add_argument("--action", type=str, choices=["s", "p"], help="save or print")

		try:
			self.cmd_arguments = parser.parse_args()
		except SystemExit as e:
			self.cmd_arguments = -1
			# print (e)

	def get_cmd_arguments(self):
		return self.cmd_arguments
