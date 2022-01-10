#####was man braucht#####

print("Hi, wir tragen schnell die Daten ein, welche mein Programm braucht.\nDu musst das nur einmal machen, ausser du verkackst was oder wechselst die Abteilung oder sowas."
      "\nEinfach so eintragen, wie es in der bsp.txt datei gezeigt wird.")
print("-----------------------------------------------------------------------")

NrBerichtsheft=input("Gib die Nummer an bei welchem Berichtsheft du jetzt bist: ")
NameBerichtsheft= input("Dokumentenname deines Berichtshefts: ")
Ausbildungsjahr=input("In welchem Ausbildungsjahr bist du?: ")
Vorname=input("Dein Vorname: ")
Nachname=input("Dein Nachname: ")
print("Jetzt die täglichen Aufgaben eintragen, wenn fertig einfach Enter drücken.\nEs ist wichtig, so viele Aufgaben wie nur möglich hier aufzuschreiben")

inputing=True
aufgaben=[]
an=1
while inputing == True:

    try:
        TäglicheAufgabe = input("Tägliche Aufgabe Nr. "+str(an)+": ")
        if TäglicheAufgabe != "":
            aufgaben.append(TäglicheAufgabe + ", ")
            an=an+1
        else:
            inputing=False
    except:
        inputing=False




with open("datasheet.txt","w") as data:
    data.write(NrBerichtsheft+', '+NameBerichtsheft+', '+Ausbildungsjahr+', '+Vorname+" "+Nachname+', ')
    data.close()
with open("datasheet.txt","a") as data:
    for i in aufgaben:
        data.write(i)
    data.close()
print("Fertig :D \nViel Spaß wünscht dir der Matze! \nEnter drücken zum beenden, dann kannst du die Berichtsheftmaschine9000.exe starten!")
input("")

###Matthias Fuchs 19.05.2021###