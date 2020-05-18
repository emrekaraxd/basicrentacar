# created abstract class for car interface
from abc import ABCMeta, abstractmethod

class ICars(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def Renthourly(self, hour):
        self.hour = hour
        pass

    @abstractmethod
    def Rentdaily(self, day):            # prepare all abstract methods
        self.day = day
        pass

    @abstractmethod
    def Bill(self):
        pass
    