
class Subject:
    observers = []

    def register(self, observer):
        """Registeres an observer

        Args:
            observer (obj): An observer object to register.
        """
        if observer not in self.observers:
            self.observers.append(observer)

    def deregister(self, observer):
        """Deregister an observer

        Args:
            observer (obj): An observer to deregister.
        """
        self.observers.remove(observer)

    def notify(self, message=''):
        """Notify observers.

        Args:
            message (str, optional): A message to be sent to the registered 
                observers. Value defaults to an empty string.
        """
        for observer in self.observers:
            observer.update(message)