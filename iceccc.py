Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import csv

class IceCream:
    def __init__(self, flavor, price):
        self.flavor = flavor
        self.price = price

    def to_csv_row(self):
        return [self.flavor, self.price]

def display_menu():
    flavors = {
        "Vanilla": 3.99,
        "Chocolate": 4.99,
        "Strawberry": 4.49,
        "Mint Chocolate Chip": 5.49
    }
    scoops = {
        "Single Scoop": 1,
        "Double Scoop": 2,
        "Triple Scoop": 3
    }
    cones = {
        "Sugar Cone": 0.5,
        "Waffle Cone": 1,
        "Cup": 0
    }

    print("Ice Cream Menu:")
    print("Flavors:")
    for flavor in flavors:
        print("- " + flavor)
    print("\nScoops:")
...     for scoop in scoops:
...         print("- " + scoop)
...     print("\nCones:")
...     for cone in cones:
...         print("- " + cone)
... 
...     return flavors, scoops, cones
... 
... def calculate_total_price(flavors, scoops, cones, flavor_choice, scoop_choice, cone_choice):
...     total_price = flavors[flavor_choice] * scoops[scoop_choice] + cones[cone_choice]
...     return total_price
... 
... def display_billing(flavor_choice, scoop_choice, cone_choice, total_price):
...     print("\nBilling Information:")
...     print("--------------------")
...     print("Item\t\tPrice")
...     print("--------------------")
...     print(f"{flavor_choice}\t\t${total_price:.2f}")
...     print(f"Scoops: {scoop_choice}")
...     print(f"Cone: {cone_choice}")
...     print("--------------------")
...     print(f"Total Price:\t${total_price:.2f}")
... 
... def save_billing_to_csv(flavor_choice, scoop_choice, cone_choice, total_price, csv_file):
...     with open(csv_file, mode='w', newline='') as file:
...         writer = csv.writer(file)
...         writer.writerow(["Item", "Scoops", "Cone", "Price"])
...         writer.writerow([flavor_choice, scoop_choice, cone_choice, total_price])
... 
... # Display the ice cream menu
... flavors, scoops, cones = display_menu()
... 
... # User input for ice cream selection
... flavor_choice = input("Choose a flavor: ")
... scoop_choice = input("Choose the number of scoops: ")
... cone_choice = input("Choose the type of cone: ")
... 
... # Calculate the total price
... total_price = calculate_total_price(flavors, scoops, cones, flavor_choice, scoop_choice, cone_choice)
... 
... # Display the billing information
... display_billing(flavor_choice, scoop_choice, cone_choice, total_price)
... 
... # Save billing information to CSV
... csv_file = "billing.csv"
... save_billing_to_csv(flavor_choice, scoop_choice, cone_choice, total_price, csv_file)
