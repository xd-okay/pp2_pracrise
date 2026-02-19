class car:
    seats_count=4
    wheels_count=4
    def get_seats(self):
        return self.seats_count
    
    def get_wheel_count(self):
        return self.wheels_count
    def get_max_speed(self):
        return 100
    
class race_car(car):
    def __init__(self):
        self.seats_count=2
    
    def get_max_speed(self):
        return 200
        
    
        
car1=car()
print(car1.get_seats())
print(car1.get_wheel_count())
print(car1.get_max_speed())

race_car1=race_car()
print(race_car1.get_seats())
print(race_car1.get_wheel_count())
print(race_car1.get_max_speed())