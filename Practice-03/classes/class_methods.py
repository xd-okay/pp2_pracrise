class car:
    mark=""
    year=0
    def set_mark(self, novaya_marka):
        self.mark=novaya_marka
        
        
    def __init__(self, brand):
        self.mark = brand    
    
    def get_mark(self):
        return self.mark
    
    def set_year(self, a):
        self.year=a

    def get_year(self):
        return self.year
b=int(input())
camry=car("BMW")
print(camry.get_mark(), camry.get_year())
camry.set_mark("Toyota")
camry.set_year(b)

print(camry.get_mark(), camry.get_year())


