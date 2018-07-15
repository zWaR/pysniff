from abc import ABCMeta, abstractmethod

class Observer(metaclass=ABCMeta):

    @abstractmethod
    def update(self, message=''):
        """Update the observers

        Args:
            message (str, optional): A message to deliver to the observers.
                Defaults to an empty string.
        """