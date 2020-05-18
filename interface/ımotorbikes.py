from abc import ABCMeta, abstractmethod
# created abstract class for car interface
class IMotorbike(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def Renthourly(self,hour):
        self.hour = hour
        pass

    @abstractmethod
    def Rentdaily(self,day):
        self.day = day                         # prepare all abstract methods 
        pass

    @abstractmethod
    def Bill(self):
        pass