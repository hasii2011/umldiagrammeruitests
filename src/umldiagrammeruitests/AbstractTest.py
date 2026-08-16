
from abc import ABC
from abc import abstractmethod


class AbstractTest(ABC):

    @abstractmethod
    def execute(self):
        """
        Run the test from this method
        """
        pass
