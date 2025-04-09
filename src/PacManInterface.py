from abc import ABC, abstractmethod

class PacManInterface(ABC):
	@abstractmethod
	def get_packages(self):
		pass
