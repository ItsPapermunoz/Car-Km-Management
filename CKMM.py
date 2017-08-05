# Module imports

import pickle

# Variable Declarations

__version__ = "Alpha"
__author__ = "Rodrigo 'ItsPaper' Muñoz"
__authoremail__ = "rodrigo.mcuadrada@gmail.com"
car_km = []
price_km = []
car_capacity = 0
# Functions

def check_file():
    # Checks if files exist already and reads data from them if they do, creates new files prompts the user for car capacity data and returns the values...
    try:
        car_km = pickle.load(open("Car_km.data", "rb"))
        price_km = pickle.load(open("Price_km.data", "rb"))
        car_capacity = pickle.load(open("Car_Capacity.data", "rb"))
    except FileNotFoundError:
        car_km = []
        price_km = []
        try:
            car_capacity = int(input("Please enter your car's capacity in liters..."))
        except ValueError:
            car_capacity = int(input("Please enter your car's capacity in liters..."))
        pickle.dump(car_km, open("Car_km.data", "wb"))
        pickle.dump(price_km, open("Price_km.data", "wb"))
        pickle.dump(car_capacity, open("Car_Capacity.data", "wb"))
    finally:
        return car_km, price_km, car_capacity


def prompt_entry():
    try:
        km_entry = int(input("Please enter the amount of kilometers driven in a full tank..."))
    except:
        return 1
    try:
        price_entry = int(input("Please enter the cost to fill the tank..."))
    except:
        return 1
    entries = [km_entry, price_entry]
    return entries


def confirmation():
    confirm = input("Do you wish to confirm? Y-N")
    confirm = confirm.lower()
    if confirm == "yes" or confirm == "y":
        return True
    else:
        print("Confirmation Failed!")
        return False

def new_entry():
    entries = prompt_entry()
    if entries == 1:
        print("Entry Failed...")
        return
    else:
        km_entry, price_entry = entries
    car_km.append(km_entry)
    price_km.append(price_entry)
    confirm = confirmation()
    if confirm:
        pickle.dump(car_km, open("Car_km.data", "wb"))
        pickle.dump(price_km, open("Price_km.data", "wb"))
        print("Entries Dumped Correctly!")


def read_entries():
    i = 0
    total_km = 0
    total_price = 0
    max_range = 0
    min_range = 1000
    for entry in car_km:
        entry_number = i + 1
        km_per_l = entry / car_capacity
        print("Entry Number: {}\nKilometers driven: {}\nCost of this tank: {}".format(entry_number, entry, price_km[i]))
        print("Kilometers per liter: {}\n".format(km_per_l))
        total_km += entry
        total_price += price_km[i]
        if entry > max_range:
            max_range = entry
        if entry < min_range:
            min_range = entry
        i += 1
    print("Total entries: {}\nTotal Kilometers Recorded: {}".format(entry_number, total_km))
    print("Total Costs Recorded: {}".format(total_price))
    print("Highest range: {}\nLowest Range:{}".format(max_range, min_range))


def delete_entry():
    i = 0
    for entry in car_km:
        entry_number = i + 1
        km_per_l = entry / car_capacity
        print("Entry Number: {}\nKilometers driven: {}\nCost of this tank: {}".format(entry_number, entry, price_km[i]))
        print("Kilometers per liter: {}\n".format(km_per_l))
        i += 1
    try:
        entry_selection = int(input("Which entry would you like to delete..."))
    except ValueError:
        print("Entry Deletion Failed")
        return
    finally:
        if entry_selection > entry_number:
            print("Entry number {} does not exist...".format(entry_selection))
            return
        entry_selection -= 1
        confirm = confirmation()
        if confirm:
            car_km.remove(car_km[entry_selection])
            price_km.remove(price_km[entry_selection])
            pickle.dump(car_km, open("Car_km.data", "wb"))
            pickle.dump(price_km, open("Price_km.data", "wb"))
            print("Entry Deleted succesfully!")


def menu():

# Main Code

car_km, price_km, car_capacity = check_file()
read_entries()
