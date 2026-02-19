nums=list(map(int, input().split()))
even_list=lambda s: list(filter( lambda x: x%2==0, s))
print(even_list(even_list(nums)))



