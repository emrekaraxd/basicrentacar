from interface.ıcars import ICars

class Car(ICars):

    def __init__(self):
        super(Car, self).__init__()
        self.bill = 1

    def Renthourly(self, hour):
        self.bill = hour * 100
        with open("billstock.txt","a") as file:
            bill = str(self.bill)
            file.write(f"Rented car {hour} hourly for {bill} dolar." + "\n")
        print("Your rental successful.")
        return self.bill


    def Rentdaily(self, day):
        self.bill = day * 1500
        with open("billstock.txt","a") as file:
            bill = str(self.bill)
            file.write(f"Rented car {day} day for {bill} dolar." + "\n")
        print("Your rental successful.")
        return self.bill

    def Bill(self):
        print(f"Your rental cost {self.bill}")