from interface.ımotorbikes import IMotorbike

class Motorbike(IMotorbike):

    def __init__(self):
        super(Motorbike, self).__init__()
        self.bill = 1

    def Renthourly(self,hour):
        self.bill = hour * 50
        with open("billstock.txt","a") as file:
            bill = str(self.bill)
            file.write(f"Rented motorbike {hour} hourly for {bill} dolar." + "\n")
        print("Your rental successful.")
        return self.bill

    def Rentdaily(self,day):
        self.bill = day * 1000
        with open("billstock.txt","a") as file:
            bill = str(self.bill)
            file.write(f"Rented motorbike {day} day for {bill} dolar." + "\n")
        print("Your rental successful.")
        return self.bill

    def Bill(self):
        print(f"Your rental cost {self.bill}")