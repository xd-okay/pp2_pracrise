class car:
    country =""
    def __init__(self, country):
        self.country=country
        
class race_car(car):
    max_speed=0
    def __init__(self, country, max_speed):
        super().__init__(country)
        self.max_speed =max_speed
    
    
porshe=race_car("Germany", 200)
print(porshe.country, porshe.max_speed)

ferrari_tracktor=race_car("Italy", 15 )
print(ferrari_tracktor.country, ferrari_tracktor.max_speed)