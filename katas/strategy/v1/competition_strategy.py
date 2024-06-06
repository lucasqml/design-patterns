from abc import ABC, abstractmethod

class CompetitionStrategy(ABC):
    @abstractmethod
    def compete(self):
        pass