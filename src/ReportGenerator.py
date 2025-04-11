from PacManInterface import PacManInterface

class ReportGenerator():
	softwareInstalled = None
	report = None

	def __init__(self):
		pacmanInterface = PacManInterface()
		hardwareParser = None # update this with hardware parser

		self.softwareInstalled = pacmanInterface.get_packages()

	def format_report(self, fileFormat):
		if(fileFormat == "txt"):
			self.report = self.softwareInstalled
		elif(fileFormat == "csv"):
			self.report = self.softwareInstalled
			self.report = self.report.replace(" ", ",")
			self.report = "Software, Version\n" + self.report
			print(self.report)
		elif(fileFormat == "json"):
			self.report = "{\n\t\"software\": ["
			for software in self.softwareInstalled.split("\n"):
				name, version = software.split(" ")
				self.report = self.report + "\n\t\t{\n\t\t\t\"name\": \"" + name + "\",\n\t\t\t\"version\": \"" + version + "\"\n\t\t},"
			self.report = self.report[:-1]
			self.report = self.report + "\n\t]\n}"

	def print_report(self, fileFormat):
		self.format_report(fileFormat)
		print(self.report)

	def save_report(self, fileFormat):
		self.format_report(fileFormat)
		with open(f"report.{fileFormat}", "w") as file:
			file.write(self.report)
		print("Report saved!")
		pass
