power = {
    "battery_percentage": 35
}

character = {
    "name": "Worker",
    "class": "Engineer",
    "level": 1,
    "exp": 1,
    "inventory": { }
}


def check_user_input(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("\n Please select one of the options")
            continue
        else:
            return userInput
            break

def check_station_power():
    print("Station power is currently at {}%".format(power["battery_percentage"]))

def game_intro():
    return "Hello {char_name}, you are an {char_class}, your job is to keep the power station alive.\nIf the power goes off, you lose. To do this you need to use your drones to acquire materials and use them to repair your station through this terminal.".format(char_name = character["name"], char_class = character["class"])

def check_inventory():
    print("\nInventory")
    for item in character["inventory"]:
        print("\n {item}: {quantity}".format(item = item, quantity = character["inventory"][item]))

def check_drones(drones):
    print("\nDrones")
    for drone in drones:
        print("\n \n {}".format(drone))

def select_zone(zones):
    print("Select Zone")
    zone_select = ""
    while True:
        for x in range(len(zones)):
            print("\n{x}){zone}".format(x = x+1, zone = zones[x]))
        print("\n7) Go Back")
        user_select = check_user_input("Select Zone to continue")
        if user_select == 7:
            break
        elif user_select in range(1, len(zones) + 1):
            zone_select = zones[user_select - 1]
            break
    return zone_select
            