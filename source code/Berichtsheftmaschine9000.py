from mailmerge import MailMerge

def fertigmachen():

    fertig= input("Fertig? Y/N: ")
    if fertig=="Y" or fertig == "y":
        with open("datasheet.txt", "w") as enddata:
            enddata.write(str(BNrneu)+', '+Name+', '+Jahr+', '+NameIch+', '+TäglicheAufgabe1+', '+TäglicheAufgabe2+', '+TäglicheAufgabe3+', '+TäglicheAufgabe4+', '+TäglicheAufgabe5)
            enddata.close()
            print("Dokument erfolgreich erzeugt (hoffentlich)!")
            print("Enter drücken um das Programm zu schließen! \nBis dann :)")
            input("")
    elif fertig=="N" or fertig == "n":
        print("Dokument erfolgreich erzeugt (hoffentlich)!")
        with open("datasheet.txt", "w") as enddata:
            enddata.write(str(BNrneu)+', '+Name+', '+Jahr+', '+NameIch+', '+TäglicheAufgabe1+', '+TäglicheAufgabe2+', '+TäglicheAufgabe3+', '+TäglicheAufgabe4+', '+TäglicheAufgabe5)
            enddata.close()
        berichtsheftmaschine9000()
    else:
        print("Falsche Eingabe!")
        with open("datasheet.txt", "w") as enddata:
            enddata.write(str(BNrneu)+', '+Name+', '+Jahr+', '+NameIch+', '+TäglicheAufgabe1+', '+TäglicheAufgabe2+', '+TäglicheAufgabe3+', '+TäglicheAufgabe4+', '+TäglicheAufgabe5)
            enddata.close()
        fertigmachen()

def berichtsheftmaschine9000():
    #Gespeicherte Daten einlesen
    with open("datasheet.txt") as data:
        inhalt=data.read()
        datalist=inhalt.split(', ')

    #Werte Verteilen Header
    global BNr,Name,Jahr,NameIch
    BNr=datalist[0]
    print("Berichtsheft Nr.: "+BNr)
    Name=datalist[1]
    Jahr=datalist[2]
    NameIch = (datalist[3])
    Datum1=input("Woche vom: ")
    Datum2= input("bis zum: ")

    #############Wochentage bearbeiten################

    Wochentag=["Montag","Dienstag","Mittwoch","Donnerstag","Freitag"]
    Aktivität=range(5)

    global TäglicheAufgabe1,TäglicheAufgabe2,TäglicheAufgabe3,TäglicheAufgabe4,TäglicheAufgabe5

    TäglicheAufgabe1=datalist[4]
    TäglicheAufgabe2=datalist[5]
    TäglicheAufgabe3=datalist[6]
    TäglicheAufgabe4=datalist[7]
    TäglicheAufgabe5=datalist[8]

    presets=[datalist[4],datalist[5],datalist[6],datalist[7],datalist[8]]
    wochenaktivitäten=[]
    #print(len(wochenaktivitäten))

    for Tag in range(len(Wochentag)):
        print(Wochentag[Tag])
        print("1: "+TäglicheAufgabe1+"\n2: "+TäglicheAufgabe2+"\n3: "+TäglicheAufgabe3+"\n4: "+TäglicheAufgabe4+"\n5: "+TäglicheAufgabe5+"\n0: Eigene Eingabe")
        for Aktiv in range(len(Aktivität)):
            print(Wochentag[Tag]+" Aktivität "+str(Aktiv+1)+": ")
            reinschreiben=input()
            if reinschreiben == "":
                wochenaktivitäten.append(" ")
            if reinschreiben != "0":
                try:
                    wochenaktivitäten.append(presets[int(reinschreiben)-1])
                except:
                    pass
            else:
                wochenaktivitäten.append(input("Inhalt: "))

    #print(wochenaktivitäten)


    ###########Ausfüllen##############

    with MailMerge ("Berichtsheft_Vorlage.docx") as dokument:
        feldname = (dokument.get_merge_fields())
        #print(feldname)
        dokument.merge(Nachweisnummer=BNr,Datum1=Datum1,Datum2=Datum2,Jahr=Jahr,Name=NameIch,
                       a1=wochenaktivitäten[0],a2=wochenaktivitäten[1],a3=wochenaktivitäten[2],a4=wochenaktivitäten[3],a5=wochenaktivitäten[4],
                       b1=wochenaktivitäten[5],b2=wochenaktivitäten[6],b3=wochenaktivitäten[7],b4=wochenaktivitäten[8],b5=wochenaktivitäten[9],
                       c1=wochenaktivitäten[10],c2=wochenaktivitäten[11],c3=wochenaktivitäten[12],c4=wochenaktivitäten[13],c5=wochenaktivitäten[14],
                       d1=wochenaktivitäten[15],d2=wochenaktivitäten[16],d3=wochenaktivitäten[17],d4=wochenaktivitäten[18],d5=wochenaktivitäten[19],
                       e1=wochenaktivitäten[20],e2=wochenaktivitäten[21],e3=wochenaktivitäten[22],e4=wochenaktivitäten[23],e5=wochenaktivitäten[24])
        dokument.write(str(BNr)+Name+Datum1+"-"+Datum2+".docx")
    global BNrneu
    BNrneu = int(BNr) + 1
    fertigmachen()




def checkdatasheet():
    try:
        open("datasheet.txt")
    except FileNotFoundError:
        print("Bitte zuerst initial.exe laufen lassen!")
        input("Enter drücken zum beenden")
    else:
        berichtsheftmaschine9000()
checkdatasheet()






###Matthias Fuchs 19.05.2021###


