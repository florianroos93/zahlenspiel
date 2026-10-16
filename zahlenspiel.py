import random
durchgang = 1
zufallszahl = random.randint(1, 10)
while durchgang <8:
    print(durchgang)
    durchgang = durchgang +1
    benutzereingabe = input()
    benutzereingabe = int(benutzereingabe)
    if benutzereingabe < zufallszahl:
          print("Die geheime Zahl ist größer als deine Eingabe.")
    elif benutzereingabe > zufallszahl:
        print("Die geheime Zahl ist kleiner als deine Eingabe.")





if int(benutzereingabe) == zufallszahl:
        print("Gewonnen! Die geheime Zahl ist nicht mehr geheim!")
        
else:
     print("Schade – verloren. Einfach nochmals probieren!")

