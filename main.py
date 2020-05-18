from customermenu import Customer
from cars import Car
from carstock import Carstock
from motorbikes import Motorbike

# import all object

customer = Customer(Car(),Carstock(),Motorbike())

main_menu = True

while True:

    if main_menu:
        print("""
        *************VEHİCLE RENTAL SHOP*************
        C - Rent a car
        B - Rent a motorbike
        E - Exit
        """)
        main_menu = False

        choice = input("Your choice: ")


        if choice == "C" or choice == "c":

            print("""
            *************CAR MENU*************
            1 - Display car stock
            2 - Request a car for hourly
            3 - Request a car for daily
            4 - Return a car
            5 - Main menu
            6 - Exit
            """)

            key = input("Your choice: ")

            if key == "1":
                # customer can see all car stock
                customer.Getstock_carstock()
                main_menu = True

            elif key == "2":
                print("Hourly rental fee 100 dolar per hours.")
                hour = int(input("Enter how many hours you will rent: "))

                customer.Renthourly_cars(hour)
                caramount = 1
                customer.Uptadestock_carstock(caramount)
                #rezerve

                main_menu = True

            elif key == "3":
                print("Daily rental fee 1500 dolar per hours.")
                day = int(input("Enter how many day you will rent: "))
                
                customer.Rentdaily_cars(day)
                caramount = 1
                customer.Uptadestock_carstock(caramount)
                #rezerve

                main_menu = True
            
            elif key == "4":
                print("Thank you for bringing the car back. We will wait again.")
                customer.Bill_cars()

                main_menu = True
            
            elif key == "5":
                main_menu = True
            
            elif key == "6":
                break
            
            else:
                print("Hatalı tuşlama.")
                main_menu = True


        elif choice == "B" or choice == "b":

            print("""
            *************MOTORBIKE MENU*************
            1 - Display bike stock
            2 - Request a bike for hourly
            3 - Request a bike for daily
            4 - Return a bike
            5 - Main menu
            6 - Exit
            """)

            key = input("Your choice: ")

            if key == "1":
                # customer can see all bike stock
                customer.Getstock_carstock()
                main_menu = True

            elif key == "2":
                print("Hourly rental fee 50 dolar per hours.")
                hour = int(input("Enter how many hours you will rent: "))

                customer.Renthourly_bikes(hour)
                caramount = 1
                customer.Uptadestock_carstock(caramount)
                #rezerve

                main_menu = True

            elif key == "3":
                print("Daily rental fee 1000 dolar per hours.")
                day = int(input("Enter how many day you will rent: "))
                
                customer.Rentdaily_bikes(day)
                caramount = 1
                customer.Uptadestock_carstock(caramount)
                #rezerve

                main_menu = True
            
            elif key == "4":
                print("Thank you for bringing the motorbike back. We will wait again.")
                customer.Bill_bikes()

                main_menu = True
            
            elif key == "5":
                main_menu = True
            
            elif key == "6":
                break
            
            else:
                print("Hatalı tuşlama.")
                main_menu = True

        elif choice == "E" or choice == "e":
            break


        else:
            print("Wrong selection.")
            break


        








