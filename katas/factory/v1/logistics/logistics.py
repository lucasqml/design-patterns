from abc import ABC, abstractmethod

class Logistics(ABC):
    @abstractmethod
    def create_transport(self):
        pass