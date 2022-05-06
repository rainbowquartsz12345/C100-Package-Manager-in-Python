#OOP - Object Oriented Programming.
class car(object):
    def __init__(self, model, color, company, speed_limit):
        self.model = model
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
    def start(self):
        print("Started ....")
    def stop(self):
        print("Stop the car")
    def accelerate(self):
        print("Going Faster")
     
#creating object for the class car
audi = car("A6", "black" , "Audi","100")
print(  audi.start() )
print(audi.color)

Toyota = car("Corolla", "White", "Toyota", "120" )
print(Toyota.accelerate())