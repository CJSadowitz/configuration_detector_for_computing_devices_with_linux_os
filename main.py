from src.ArgumentParser  import ArgumentParser
from src.HardwareParser  import HardwareParser
from src.PacManInterface import PacManInterface
from src.ReportGenerator import ReportGenerator

def main():
	parser = ArgumentParser()
	packages = PacManInterface()
	hardware = HardwareParser()
	args = parser.get_cmd_arguments()
	software, cpu_info, mem_info, devices, linux_ver = "", [], [], [], ""
	if args.get_packages:  software  = packages.get_packages()
	if args.get_CPU_info:  cpu_info  = hardware.get_CPU_info()
	if args.get_mem_info:  mem_info  = hardware.get_mem_info()
	if args.get_devices:   devices   = hardware.get_devices()
	if args.get_linux_ver: linux_ver = hardware.get_linux_ver()
	if args.action == "s": ReportGenerator(software, cpu_info, mem_info, devices, linux_ver).save_report(args.file_type)
	if args.action == "p": ReportGenerator(software, cpu_info, mem_info, devices, linux_ver).print_report(args.file_type)

if __name__ == "__main__":
	main()
