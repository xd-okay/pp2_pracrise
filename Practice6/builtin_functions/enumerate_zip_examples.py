names=["Aldiyar", "Adilkhan", "Dayana", "Alina", "Iliyas"]
number=[i for i in range(len(names)+1)]
for i, name in enumerate(names):
    print(i+1, name)
    
    
big_list=list(zip(names, number))
print(big_list)
    
