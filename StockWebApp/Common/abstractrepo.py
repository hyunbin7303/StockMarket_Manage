# Importing the ABC (Abstract Base Class) module from the abc package
from abc import ABC, abstractmethod

# Defining an abstract class called AbstractRepository that inherits from ABC
class AbstractRepository(ABC):

    # Defining an abstract method called add that takes one argument, 'chocolate_box'
    @abstractmethod
    def add(self, chocolate_box):
        # This method will be implemented by the concrete repositories
        pass

    # Defining an abstract method called get that takes one argument, 'id'
    @abstractmethod
    def get(self, id):
        # This method will be implemented by the concrete repositories
        pass

    # Defining an abstract method called remove that takes one argument, 'chocolate_box'
    @abstractmethod
    def remove(self, chocolate_box):
        # This method will be implemented by the concrete repositories
        pass