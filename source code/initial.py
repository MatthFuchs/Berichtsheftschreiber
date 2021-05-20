#####was man braucht#####

print("Hi, wir tragen schnell die Daten ein, welche mein Programm braucht.\nDu musst das nur einmal machen, ausser du verkackst was."
      "\nEinfach so eintragen, wie es in der bsp.txt datei gezeigt wird.")
print("-----------------------------------------------------------------------")

NrBerichtsheft=input("Gib die Nummer an bei welchem Berichtsheft du jetzt bist: ")
NameBerichtsheft= input("Dokumentenname deines Berichtshefts: ")
Ausbildungsjahr=input("In welchem Ausbildungsjahr bist du?: ")
Vorname=input("Dein Vorname: ")
Nachname=input("Dein Nachname: ")

try:
    TäglicheAufgabe1=input("Tägliche Aufgabe Nr. 1: ")
except:
    TäglicheAufgabe1 =" "
try:
    TäglicheAufgabe2=input("Tägliche Aufgabe Nr. 2: ")
except:
    TäglicheAufgabe2=" "
try:
    TäglicheAufgabe3=input("Tägliche Aufgabe Nr. 3: ")
except:
    TäglicheAufgabe3=" "
try:
    TäglicheAufgabe4=input("Tägliche Aufgabe Nr. 4: ")
except:
    TäglicheAufgabe4=" "
try:
    TäglicheAufgabe5=input("Tägliche Aufgabe Nr. 5: ")
except:
    TäglicheAufgabe5=" "



with open("datasheet.txt","w") as data:
    data.write(NrBerichtsheft+', '+NameBerichtsheft+', '+Ausbildungsjahr+', '+Vorname+" "+Nachname+', '+TäglicheAufgabe1+', '+TäglicheAufgabe2+', '+TäglicheAufgabe3+', '+TäglicheAufgabe4+', '+TäglicheAufgabe5)
    data.close()

print("Fertig :D \nViel Spaß wünscht dir der Matze! \nEnter drücken zum beenden, dann kannst du die Berichtsheftmaschine9000.exe starten!")
input("")

###Matthias Fuchs 19.05.2021###