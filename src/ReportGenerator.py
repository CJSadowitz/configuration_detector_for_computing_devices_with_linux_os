class ReportGenerator():
	softwareInstalled = None
	cpuInfo = None
	memInfo = None
	devicesInfo = None
	linuxVer = None
	report = None

	def __init__(self, packageInfo="", cpuInfo=[], memInfo=[], devicesInfo=[], linuxVer=""):
		self.softwareInstalled = packageInfo
		self.cpuInfo     = cpuInfo
		self.memInfo     = memInfo
		self.devicesInfo = devicesInfo
		self.linuxVer    = linuxVer

	def format_report(self, fileFormat):
		if(fileFormat == "txt"):
			self.report = "=== Software Installed ===\n"
			self.report += self.softwareInstalled + "\n\n"

			self.report += "=== CPU Info ===\n"
			self.report += "\n".join(self.cpuInfo) + "\n\n"

			self.report += "=== Memory Info ===\n"
			self.report += "\n".join(self.memInfo) + "\n\n"

			self.report += "=== Devices ===\n"
			self.report += "\n".join(self.devicesInfo) + "\n\n"

			self.report += "=== Linux Version ===\n"
			self.report += self.linuxVer + "\n\n"
		elif(fileFormat == "csv"):
			self.report = self.softwareInstalled
			self.report = self.report.replace(" ", ",")
			self.report = "Software, Version\n" + self.report

			# break report into a list of at least the required number of rows
			rows = 1 + max(1, len(self.cpuInfo), len(self.memInfo), len(self.devicesInfo))
			self.report = self.report.split("\n")
			while len(self.report) < rows:
				self.report.append("")

			self.report[0] += ",,Linux Version,,CPU,Memory,Devices"
			for r in range(1, rows):
				if r == 1:
					self.report[r] += ",," + self.linuxVer.replace(",", " ") + ",,"
				else:
					self.report[r] += ",,,,"
				if len(self.cpuInfo) > r - 1:
					self.report[r] += self.cpuInfo[r - 1] + ","
				else:
					self.report[r] += ","
				if len(self.memInfo) > r - 1:
					self.report[r] += self.memInfo[r - 1] + ","
				else:
					self.report[r] += ","
				if len(self.devicesInfo) > r - 1:
					self.report[r] += self.devicesInfo[r - 1] + ","
				else:
					self.report[r] += ","

			self.report = "\n".join(self.report)
		elif(fileFormat == "json"):
			# print software installed
			self.report = "{\n\t\"software\": ["
			if self.softwareInstalled != "":
				for software in self.softwareInstalled.split("\n"):
					name, version = software.split(" ")
					self.report = self.report + "\n\t\t{\n\t\t\t\"name\": \"" + name + "\",\n\t\t\t\"version\": \"" + version + "\"\n\t\t},"
			self.report = self.report[:-1]
			self.report = self.report + "\n\t],\n"

			# print Linux version
			self.report += "\t\"linux-version\": \"" + self.linuxVer +"\",\n"

			# print CPU info
			self.report += "\t\"cpu\": ["
			for cpu in self.cpuInfo:
				self.report += "\n\t\t\"" + cpu + "\","
			self.report = self.report[:-1]
			self.report += "\n\t],\n"

			# print memory info
			self.report += "\t\"memory\": ["
			for mem in self.memInfo:
				self.report += "\n\t\t\"" + mem + "\","
			self.report = self.report[:-1]
			self.report += "\n\t],\n"

			# print devices
			self.report += "\t\"devices\": ["
			for dev in self.devicesInfo:
				self.report += "\n\t\t\"" + dev + "\","
			self.report = self.report[:-1]
			self.report += "\n\t]\n}\n"

	def print_report(self, fileFormat):
		self.format_report(fileFormat)
		print(self.report)

	def save_report(self, fileFormat):
		self.format_report(fileFormat)
		with open(f"report.{fileFormat}", "w") as file:
			file.write(self.report)
		print("Report saved!")
