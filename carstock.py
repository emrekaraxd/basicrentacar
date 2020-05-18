from interface.ıcarstock import ICarStock

class Carstock(ICarStock):

    def __init__(self):
        super(Carstock, self).__init__()
        self.carstocks = 15
        self.bikestock = 5

    def Getstock(self):
        print(f"""
        {self.carstocks} car available for rent.
        {self.bikestock} bike available for rent.
        
        """)

    def Uptadestock(self, number):
        pass

        
        





    