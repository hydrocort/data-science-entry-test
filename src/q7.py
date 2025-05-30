class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """
    def __init__(self, make, model, year):
        """
        Constructor method that sets up the initial attributes of each car
        """
        self.make = make    
        self.model = model  
        self.year = year    

    def describe_car(self):
        """
        This method prints information about the car in the format "Year Make Model"
        """
        print(f"{self.year} {self.make} {self.model}")

# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020

print("=== Testing Car Class ===")
print()

# Create a new car object using our Car class blueprint
my_car = Car("Toyota", "Corolla", 2020)

# Call the describe_car method to display the car information
print("Car description:")
my_car.describe_car()