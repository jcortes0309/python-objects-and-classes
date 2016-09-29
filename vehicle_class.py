# Create a class Vehicle. A Vehicle object will have 3 attributes:
class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print "\n%d %s %s" % (self.year, self.make, self.model)


# A vehicle is created
car = Vehicle("Nissan", "Leaf", 2015)

print "\nThe car is a %d %s %s" % (car.year, car.make, car.model)

# Add a print_info method to the Vehicle class
car.print_info()
