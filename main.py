import random
from game_classes import drones, zones, Zone
from functions import *

def play(char):
    game_continue = True
    print(game_intro())
    while game_continue:
        user_choice = input("\nHow would you like to proeceed? \n \n 1) Check Station Power \n \n 2) Check Inventory \n \n 3) Check Drones \n \n 4) Exploration \n \n 5) Exit")
        if user_choice == "1":
            check_station_power()
            input("\nPress any key to continue!")
        elif user_choice == "2":
            check_inventory()
            input("\nPress any key to continue!")
        elif user_choice == "3":
            check_drones(drones)
            input("\nPress any key to continue!")
        elif user_choice == "4":
            zone_selected = select_zone(zones)
            print("\n Zone Selected:", zone_selected.zone_name)
            input("\nPress any key to continue!")
            zone_selected.exploration(char, drones)
            input("\nPress any key to continue!")
        elif user_choice == "5":
            break
        else:
            "Please select an option"
            
play(character)