from abc import ABCMeta, abstractmethod
# created abstract class for car interface
class ICarStock(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def Getstock(self):
        pass
                                                           # prepare all abstract methods
    @abstractmethod
    def Uptadestock(self,number):
        pass


