producs = ["p1", "p2", "p3", "p4", "p1"]

while producs.count("p1") > 0:
    producs.remove("p1")

print(producs)

producs = ["p1", "p2", "p3", "p4", "p1"]

while 'p1' in producs:
    producs.remove("p1")

print(producs)

