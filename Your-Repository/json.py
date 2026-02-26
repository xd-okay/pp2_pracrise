import json

with open('sample-data.json') as f:
    data=json.load(f)

for i in data["imdata"]:
    dn=i['l1PhysIf']['attributes']['dn']
    descr=i['l1PhysIf']['attributes']['descr']
    speed= i['l1PhysIf']['attributes']['speed']
    mtu=i['l1PhysIf']['attributes']['mtu']
    print("%-42s %-10s %-8s %-4s" % (dn, descr, speed, mtu))
    