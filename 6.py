# Vehicle is a parent with a start method. Car and Bike extend Vehicle, adding their behaviors (drive and ride). It demonstrates hierarchical inheritance, enabling reuse of the start method across multiple child classes with their own actions


class Vehicle:
    def start(self):
        print("Vehicle started.")


class Car(Vehicle):
    def drive(self):
        print("Car is driving.")


class Bike(Vehicle):
    def ride(self):
        print("Bike is riding.")


car = Car()
bike = Bike()


car.start()   
car.drive()   

bike.start()  
bike.ride()   
