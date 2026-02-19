nums= [("Cobalt", 6500), ("Camry", 12000), ("BMW", 18000), ("Tucson", 13000)]
sorted_vy_price=lambda s: sorted(s, key=lambda x: x[1])
print(sorted_vy_price(nums))
