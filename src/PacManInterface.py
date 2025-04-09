from abc import ABC, abstractmethod

class PacManInterface(ABC):
	def __init__(self):
		pass

	@abstractmethod
	def get_packages(self):
		pass
