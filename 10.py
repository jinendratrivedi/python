class Appliance:
    def set_data(self, brand, power):
        self.brand = brand
        self.power = power

    def display(self):
        print(f"Brand: {self.brand}, Power: {self.power}W")

class Computer:
    def set_speed(self, speed):
        self.speed = speed

    def display(self):
        print(f"Processing Speed: {self.speed} GHz")

class Laptop(Appliance, Computer):
    def set_laptop(self, brand, power, speed, battery):
        self.set_data(brand, power)
        self.set_speed(speed)
        self.battery = battery

    def display(self):
        Appliance.display(self)
        Computer.display(self)
        print(f"Battery Life: {self.battery} hours")

# Test
l = Laptop()
l.set_laptop("Lenovo", 65, 3.2, 9)
l.display()
