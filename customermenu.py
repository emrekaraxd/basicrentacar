from interface.ıcustomers import ICustomer


class Customer(ICustomer):

    def __init__(self,cars,carstock,bikes):
        super(Customer, self).__init__(cars, carstock, bikes)
        pass

    def Getstock_carstock(self):
        self.carstock.Getstock()

    def Uptadestock_carstock(self,number):
        pass

    def Renthourly_cars(self,hour):
        self.cars.Renthourly(hour)

    def Rentdaily_cars(self,day):
        self.cars.Rentdaily(day)

    def Bill_cars(self):
        self.cars.Bill()

    def Renthourly_bikes(self,hour):
        self.bikes.Renthourly(hour)

    def Rentdaily_bikes(self,day):
        self.bikes.Rentdaily(day)

    def Bill_bikes(self):
        self.bikes.Bill()

        
