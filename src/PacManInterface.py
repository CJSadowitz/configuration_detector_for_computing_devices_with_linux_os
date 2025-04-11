#from abc import ABC, abstractmethod
#
#class PacManInterface(ABC):
#	def __init__(self):
#		pass
#
#	@abstractmethod
#	def get_packages(self):
#		pass

import os

class PacManInterface:
	def __init__(self):
		pass

	def run_command(self, cmd):
		with os.popen(cmd) as stdout:
			return stdout.read().strip()

	def get_packages(self):
		try:
			with open("/etc/os-release") as os_release:
				os_info = os_release.read().lower()
			if "arch" in os_info:
				return self.run_command("pacman -Q")
			elif "ubuntu" in os_info or "debian" in os_info:
				return self.run_command("apt list --installed | awk -F'[ /]' '{print $1, $3}'")
			# and so on
		except FileNotFoundError:
			return "OS not identifiable."
