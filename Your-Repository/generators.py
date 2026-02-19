def fibu(max):
    a=0
    b=1
    temp=0
    i=0
    while(i<max):
        temp=b
        b=a+b
        a=temp
        i+=1
        yield b
    
    
a=int(input())
numbers = fibu(a)
my_iter = iter(numbers)


i=0
while(i<a):
    print(next(my_iter))
    i+=1
    
        