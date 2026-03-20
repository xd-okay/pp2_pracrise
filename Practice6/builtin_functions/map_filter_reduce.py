from functools import reduce

# nums=list(map(int, input().split()))
# even_list=lambda s: list(filter( lambda x: x%2==0, s))
# print(even_list(even_list(nums)))

nums=[1,2,3,4,5,6,7,9]
double=lambda s: list(map(lambda x: x*2, s))
print(double(nums))



numss=[1,2,3,4]
total_ssum= lambda s: reduce(lambda x,y: x+y, s)

print(total_ssum(numss))