import pyMensa

for mensa in pyMensa.available:
    print(mensa.name + " | " + ", ".join(mensa.aliases))
