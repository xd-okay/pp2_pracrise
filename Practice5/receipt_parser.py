import re


with open('raw.txt', 'r', encoding='utf-8') as f:
    txt=f.readlines()

total_cost=0
for i in range(0, len(txt)):
    b=re.search(r"^[0-9]+[.]", txt[i])
    if b:
        name=txt[i+1].strip()
        # print(name)
        price=re.search(r"[0-9 ,]+", txt[i+2])
        # print(price.group(0))
        cost=txt[i+5].strip()
        cost=cost.replace(",",".")
        cost=cost.replace(" ", "")
        total_cost+=float(cost)
        # print(cost)
        print("%-100s %-10s %8s" % (name, price.group(0), cost))
        
    time=re.search("Время:", txt[i])
    if time:
        print(txt[i][7:])
    
    payment=re.search("ИТОГО:", txt[i])
    if payment:
        print(txt[i-2][:-2])
        
        

    
print("Total", total_cost)