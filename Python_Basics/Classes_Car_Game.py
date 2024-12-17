# Name: Erik Stiefeling
# Date: Dec 4, 2024
# Description: A program to simulate a car race based on 
# speed and distance. Each car is an object with 5 attributes:
# brand, year, colour, speed, and gas/battery. There are 2 types 
# of cars: gas and electric. The program generates 5 cars with 
# the speed and gas/battery set to 0. It then checks the cars in
# by setting the gas/battery to 1000 to get them ready for the race.
# The race then starts by assigning a random speed to each car. The 
# speed is then multiplied by the length of the race in hours to get
# the total distance traveled for each car. When the race is finished
# a winner is then declared and all of the car's speed is reset to 0.

import random 

# Base class representing a generic car.
class Car:
    # Initializes a Car object.
    # Takes 4 attributes
    # brand: Brand of the car (e.g., 'Toyota').
    # year: Year of manufacture.
    # colour: Colour of the car.
    # speed: Initial speed of the car, default is 0.
    def __init__(self, brand, year, colour, speed = 0):
        self.brand = brand
        self.year = year
        self.colour = colour
        self.speed = speed

    # Returns the current speed of the car.
    def get_speed(self):
        return self.speed
    
    # Sets the speed of the car to the specified value.
    def set_speed(self, speed):
        self.speed = speed

    # Placeholder for string representation of the Car.
    def __str__(self):
        pass
    
    # Placeholder for the Car's movement logic.
    def move(self, hours):
        pass
    
# Subclass of Car for electric-powered cars.
class ElectricCar(Car):
    # Initializes an ElectricCar object.
    # Inherits from Car and adds a battery attribute.
    # battery: Initial battery level, default is 0.
    def __init__(self, brand, year, colour, speed = 0, battery = 0):
        super().__init__(brand, year, colour, speed)
        self.battery = battery
        
    # Fills the battery to full capacity (1000 units).
    def charge(self):
        self.battery = 1000
        
    # Returns a string representation of an ElectricCar.
    def __str__(self):
        return (f'ElectricCar({self.brand}, {self.year}, {self.colour}, '
                f'Speed={self.speed}, Battery={self.battery})')
    
    # A method that simulates movement of the electric-powered car.
    # Reduces battery level based on the distance traveled.
    # Take 1 attribute.
    # hours: Time in hours the car moves.
    # returns distance traveled.
    def move(self, hours):
        self.hours = hours
        distance = self.speed * self.hours
        self.battery = self.battery - distance
        return distance

# Subclass of Car for gas-powered cars.
class GasCar(Car):
    # Initializes a GasCar object.
    # Inherits from Car and adds a gas attribute.
    # gas: Initial gas level, default is 0.
    def __init__(self, brand, year, colour, speed = 0, gas = 0):
        super().__init__(brand, year, colour, speed)
        self.gas = gas

    # Fills the gas tank to full capacity (1000 units).
    def fuel(self):
        self.gas = 1000

    # Returns a string representation of a GasCar.
    def __str__(self):
        return (f'GasCar({self.brand}, {self.year}, {self.colour}, '
               f'Speed={self.speed}, Gas={self.gas})')
    
    # A method that simulates movement of the gas-powered car.
    # Reduces gas level based on the distance traveled.
    # Take 1 attribute.
    # hours: Time in hours the car moves.
    # returns distance traveled.
    def move(self, hours):
        self.hours = hours
        distance = self.speed * self.hours
        self.gas = self.gas - distance
        return distance

# Class to manage a car racing game.
class CarGame:
    # Initializes a CarGame object. Takes 4 paramaters.
    # Brands: List of car brands.
    # Colours: List of car colours.
    # Start_year: Starting year for car manufacture.
    # End_year: Ending year for car manufacture.
    def __init__(self, brands, colours, start_year, end_year):
        self.brands = brands
        self.colours = colours
        self.start_year = start_year
        self.end_year = end_year
        
    # Generates a list of random cars (ElectricCar or GasCar).
    # Takes 1 parameter.
    # num_cars: Number of cars to generate.
    def get_cars(self, num_cars):
        self.cars = []
        car_type = ['electric', 'gas']
        for car in range (num_cars):
            brand = random.choice(self.brands)
            year = random.randrange(self.start_year, self.end_year+1)
            colour = random.choice(self.colours)
            type = random.choice(car_type)
            if type == 'electric':
                self.cars.append(ElectricCar(brand, year, colour))
            else:
                self.cars.append(GasCar(brand, year, colour))
    
    # Prepares cars for the race by charging or fueling them.
    # Takes no attributes.
    # returns Tuple with counts of ElectricCars and GasCars.
    def check_cars_in(self):
        e_car, g_car= 0, 0
        for car in self.cars:
            if isinstance(car,ElectricCar):
                ElectricCar.charge(car)
                e_car+=1
            else:
                GasCar.fuel(car)
                g_car+=1
        return e_car, g_car
    
    # Simulates a race among the cars for a given duration.
    # Using a for loop create a list of car speeds and distances
    # And another for loop to check for and print the winning car
    # Takes 1 attribute 
    # hours: Duration of the race in hours.
    def car_race(self, hours):
        distances = []
        speeds = []
        for car in self.cars:
            car.speed = random.randrange(30, 101)
            speeds.append(car.speed)
            distances.append(car.move(hours))
            car.speed = 0
        winning_distance = max(distances)
        print(f'\nRace for {hours} Hours! Ready...Set...Go!\n')
        print(f'Speeds: {speeds}\n')
        print(f'Distances: {distances}\n')
        print ("The winner is:")
        for i in range(len(distances)):
            if distances[i] == winning_distance:
                print(f'\t{self.cars[i]}')
            
        

# == DO NOT MODIFY ANY CODE BELOW THIS LINE ==
    
def main():
    brands = ['Benz', 'BMW', 'Ford', 'Honda', 'Toyota']
    colors = ['Black', 'Blue', 'Grey', 'Red', 'White']
    year_start, year_end = 1999, 2023
    game = CarGame(brands, colors, year_start, year_end)

    print('== Step 1: Getting new cars ===')
    game.get_cars(5) # 5 random cars
    for car in game.cars: print(f'\t{car}') # speed & energy = 0

    print('\n== Step 2: Checking cars in race ===')
    e_car, g_car = game.check_cars_in()   
    print(f'\t## We have {e_car} ElectricCars, {g_car} GasCars.')
    for car in game.cars: print(f'\t{car}') # fully charged/fueled

    print('\n=== Step 3: Starting car race ===')
    game.car_race(5) # 5 hours race, print winners
    
    print('\n=== Step 4: Race finished ===')
    for car in game.cars: print(f'\t{car}') # check speed & energy
    print('\n== Thank You! ==\n\n')

if __name__ == '__main__':
    main()