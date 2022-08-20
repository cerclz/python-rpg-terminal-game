import random
#A class to generate zones to acquire materials

class Zone:
    def __init__(self, name, seed, distance):
        self.zone_name = name
        self.zone_seed = seed
        self.zone_distance = distance

    def __repr__(self):
        return "Name: {name}, Distance: {distance}".format(name = self.zone_name, distance = self.zone_distance)

    #Generate a crate with rewards
    def crate(self, rewards):
        rewards_crate = []
        for i in range(3):
            rewards_crate.append([rewards[i], 10])
        return rewards_crate

    #Zone exploration to gather materials
    def exploration(self, character, drones):
        selected_drone = drones[0]
        zone_crate = {reward : random.randint(0, 10) for reward in rewards}
        if selected_drone.drone_range < (self.zone_distance / 100):
            print("\nThis drone doesnt qualify for this exploration. You need one with grater value of range!")
        else:
            for key in zone_crate.keys():
                if key not in character["inventory"].keys():
                    character["inventory"][key] = zone_crate[key]
                character["inventory"][key] += zone_crate[key]
            print(character["inventory"])


#A Class to generate materials needed.
class Material:
    def __init__(self, name, cost = 1):
        self.mat_name = name
        self.mat_cost = cost

    def __repr__(self):
        return str(self.mat_name)

#A Class to generate drones
class Drone:
    max_fuel = 100
    def __init__(self, name, speed, range, fuel):
        self.drone_name = name
        self.drone_speed = speed
        self.drone_range = range
        self.drone_fuel = fuel
        self.drone_status = True
    
    def __repr__(self):
        return "Name: {}, speed: {}, range: {}, fuel: {}%".format(self.drone_name, self.drone_speed, self.drone_range, self.drone_fuel)

    def fuel_cons(self, distance):
        self.drone_fuel = self.drone_fuel - 1 / self.drone_speed * distance


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


#Generate game materials
mat_cable = Material("Cable", 5)
mat_flint = Material("Flint", 30)
mat_copper = Material("Copper", 45)
mat_gold = Material("Gold", 50)
mat_charcoal = Material("Charcoal", 30)

#Generate a list of reward with the game materials
rewards = [mat_cable, mat_flint, mat_copper, mat_gold, mat_charcoal]

#Generate Zones for exploration
zone_1 = Zone("Zone 1", 1, 287)
zone_2 = Zone("Zone 2", 2, 374)
zone_3 = Zone("Zone 3", 3, 321)
zone_4 = Zone("Zone 4", 4, 652)
zone_5 = Zone("Zone 5", 5, 185)
zone_6 = Zone("Zone 6", 6, 521)

#Add zones to list
zones = [zone_1, zone_2, zone_3, zone_4, zone_5, zone_6]

#Generate game drones
drone_1 = Drone("Drone 1", 50, 5, 10)
drone_2 = Drone("Drone 2", 60, 8, 15)


#Add drones to a list for easy import
drones = [drone_1, drone_2]










    

