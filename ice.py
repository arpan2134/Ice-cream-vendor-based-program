class IceCream:
    def __init__(self, flavor, price):
        self.flavor = flavor
        self.price = price


class IceCreamVendor:
    def __init__(self):
        self.menu = {
            "Flavors": ["Vanilla", "Chocolate", "Strawberry"],
            "Scoops": ["Single Scoop", "Double Scoop"],
            "Cones": ["Small", "Large"]
        }
        self.order_list = []
        self.total_price = 0

    def display_menu(self):
        print("Ice Cream Menu:")
        print("Flavors:")
        for index, flavor in enumerate(self.menu["Flavors"], start=1):
            print(f"{index}. {flavor}")
        print("\nScoops:")
        for index, scoop in enumerate(self.menu["Scoops"], start=1):
            print(f"{index}. {scoop}")
        print("\nCones:")
        for index, cone in enumerate(self.menu["Cones"], start=1):
            print(f"{index}. {cone}")

    def select_flavor(self):
        flavor_choice = self.get_valid_input("Select a flavor: ", len(self.menu["Flavors"]))
        flavor = self.menu["Flavors"][flavor_choice - 1]
        price = 3.99
        return IceCream(flavor, price)

    def select_scoops(self):
        scoops_choice = self.get_valid_input("Select the number of scoops (1, 2, 3): ", len(self.menu["Scoops"]))
        scoops = self.menu["Scoops"][scoops_choice - 1]
        price = 3.99 * scoops_choice
        return IceCream(scoops, price)

    def select_cone(self):
        cone_choice = self.get_valid_input("Select a cone type (1: Small, 2: Large): ", len(self.menu["Cones"]))
        cone = self.menu["Cones"][cone_choice - 1]
        price = 0.99 if cone_choice == 1 else 1.99
        return IceCream(cone, price)

    def get_valid_input(self, prompt, max_choice):
        while True:
            try:
                choice = int(input(prompt))
                if 1 <= choice <= max_choice:
                    return choice
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def add_to_order_list(self, ice_cream):
        self.order_list.append(ice_cream)
        self.total_price += ice_cream.price

    def display_billing(self):
        print("\nBilling Information:")
        print("-----------------")
        print("Item\t\tPrice")
        print("------------------")
        for order in self.order_list:
            print(f"{order.flavor}\t\t${order.price:.2f}")
        print("----------------")
        print(f"Total Price:\t${self.total_price:.2f}")

    def save_billing_to_csv(self):
     file_path = "C:/Users/arpan/OneDrive/Desktop/ice/new.csv"  
     with open(file_path, mode='w') as file:
        file.write("Item,Price\n")
        for order in self.order_list:
            file.write(f"{order.flavor},{order.price:.2f}\n")
        file.write(f"Total Price,{self.total_price:.2f}\n")



    def run(self):
     while True:
        self.display_menu()

        flavor = self.select_flavor()
        self.add_to_order_list(flavor)

        scoops = self.select_scoops()
        self.add_to_order_list(scoops)

        cone = self.select_cone()
        self.add_to_order_list(cone)

        self.display_billing()

        choice = input("Do you want to continue? (Y/N): ")
        if choice.lower() != 'y':
            self.save_billing_to_csv()  
            break

# vendorrr iceee crreaaamm programm 
vendor = IceCreamVendor()
vendor.run()
