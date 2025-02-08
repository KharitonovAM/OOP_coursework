from abc import ABC, abstractmethod
class AbsFileWork(ABC):

    @abstractmethod
    def take_data(self):
        pass

    @abstractmethod
    def write_data(self):
        pass

