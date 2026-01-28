
from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def move(self):
        pass

    def stop_engine(self):
        print('Vehicle Stoped')