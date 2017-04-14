showroom = set()

showroom.update({"Camero", "Challenger", "Aston Martin DBS", "Scion xB"})
print(len(showroom))

showroom.add("Challenger")
print(showroom)

showroom.update({"Veyron", "la Ferrari"})
print(showroom)

showroom.discard("Scion xB")
print(showroom)

junkyard = {"Camero", "la Ferrari", "Goldwing", "F150", "Gran Torino", "Tesla S"}
print(showroom.intersection(junkyard))

print(showroom.union(junkyard))



