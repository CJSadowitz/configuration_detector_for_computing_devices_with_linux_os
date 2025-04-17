import os

class PacManInterface:
	def __init__(self):
		self.packages = False

	def run_command(self, cmd):
		if cmd != "pacman -Q" and cmd != "apt list --installed | awk -F'[ /]' '{print $1, $3}'":
			return []
		with os.popen(cmd) as stdout:
			return stdout.read().strip()

	def get_packages(self):
		try:
			with open("/etc/os-release") as os_release:
				os_info = os_release.read().lower()
			if "arch" in os_info:
				self.packages = self.run_command("pacman -Q")
				return self.packages
			elif "ubuntu" in os_info or "debian" in os_info:
				self.packages = self.run_command("apt list --installed | awk -F'[ /]' '{print $1, $3}'")
				return self.packages
			# and so on
		except FileNotFoundError:
			self.packages = "OS not identifiable."
			return self.packages
