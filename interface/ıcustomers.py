from abc import ABCMeta, abstractmethod
# create one and main abstract class we can each all methods from there
class ICustomer(metaclass= ABCMeta):

    def __init__(self, cars, carstock, bikes):
        self.cars = cars
        self.carstock = carstock
        self.bikes = bikes
        pass

    @abstractmethod
    def Getstock_carstock(self):
        pass

    @abstractmethod
    def Uptadestock_carstock(self):
        pass

    @abstractmethod
    def Renthourly_cars(self):
        pass

    @abstractmethod
    def Rentdaily_cars(self):
        pass

    @abstractmethod
    def Bill_cars(self):
        pass

    @abstractmethod
    def Renthourly_bikes(self):
        pass

    @abstractmethod
    def Rentdaily_bikes(self):
        pass

    @abstractmethod
    def Bill_bikes(self):
        pass


    

