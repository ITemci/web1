

# O O P

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
        
    def add_passenger(self, name):
        if not self.open_seats(): #  if open_seats == 0
            return False
        self.passengers.append(name)
        return True
        
    def open_seats(self):
        return self.capacity - len(self.passengers)
        
        
flight = Flight(3)

people = ["harry", "ron", "draco","ginny"]

for person in people:
    
    if flight.add_passenger(person):
        print(f"person {person} was added to flight successfully")
    else:
        print(f"no available seats for {person}")
        
print(flight.passengers)

# Decoreators, Functional programming

def announce(f):
    def wrapper():
        print("About to run a function ...")
        f()
        print("Done with this function !!!")
    return wrapper

@announce
def hello():
    print("hello")
    
hello()

p = [
    {"name": "harry", "house" : "gryffindor"},
    {"name": "cho", "house" : "ravenclaw"},
    {"name": "draco", "house" : "slytherin"}
    
]

def f(person):
    return person["name"]
# or use lambda func as: 
# p.sort(key = lambda person: person["name"])

p.sort(key=f)

print(p)