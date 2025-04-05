# object-oriented
class Car:
    """General car representation"""

    def __init__(self, make, model, year):
        """Constructor method of car class."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #attribute with default

    def get_description(self):
        print(f"Car details: {self.make.upper()}, {self.model.title()}, {self.year}")
        print(f"with {self.odometer_reading} miles on it.")

    def update_odometer(self, milage):
        # new value should not be less than existing value
        # new value => milage
        # existing value => self.odometer_reading
        # when new value => existing then update to a new value
        # when new value => existing then don't update, print a message
        if milage > self.odometer_reading:
            self.odometer_reading = milage
        else:
            print(f"Odometer can not be set less than {self.odometer_reading}.")


car1 = Car('lambo', 'huracan', 2025)

# instance has access to attributes and method
# car1 object can get values of attributes, execute functions, update values of attr.
car1.get_description()
print(f"odometer reading: {car1.odometer_reading}.")
car1.odometer_reading = 120
print(f"odometer reading: {car1.odometer_reading}.")
car1.odometer_reading = 80 # this is not right based on business logic.
print(f"odometer reading: {car1.odometer_reading}.")
car1.model = 'Ferrari'

# created the method to update the odometer
car1.update_odometer(70)
car1.get_description()

