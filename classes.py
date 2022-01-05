# class point(): 
#     def __init__(self, x, y):
#         self.x = x 
#         self.y = y 

# p = point(2 ,5 )

# print(p.x)
# print(p.y)

class flight():
    def __init__(self, capacity): 
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False 
        self.passengers.append(name)
        return True

    def open_seats(self): 
        return self.capacity - len(self.passengers)

flight = flight(6) 

# people = ["Harry", "Ron", "Hermi", "Ron1", "Ron2", "Ron3"]

people = str(input(f"name:"))
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"not successfully for available for {person}")

