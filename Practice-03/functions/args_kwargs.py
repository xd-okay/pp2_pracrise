def fun(arg, list1):
    print("Info about you:")
    for i in list1:
        print(f"Your name is {arg}, info: {i}")
    

a=input()
b=list(input().split())
fun(a,b)