from mailmerge import MailMerge
import random,datetime

def datasheetwriter():
    with open("datasheet.txt", "w") as enddata:
        enddata.write(str(BNrneu) + ', ' + Name + ', ' + Jahr + ', ' + NameIch + ', ' )
        enddata.close()
    with open("datasheet.txt", "a") as enddata:
        for wert in presets:
            enddata.write(wert+", ")
        enddata.close()

def neuerdatechooser():

    global Datum1,Datum2,tagdt
    tagdtneuewoche=tagdt + datetime.timedelta(days=7)
    formatdatumneuewoche=tagdtneuewoche.strftime('%d.%m')
    Datum1=formatdatumneuewoche
    tagdt = datetime.datetime.strptime(Datum1, '%d.%m')
    tagdtneu = tagdt + datetime.timedelta(days=4)
    Datum2 = tagdtneu.strftime('%d.%m')

def fertigmachen():

    fertig= input("Fertig? Y/N: ")
    if fertig=="Y" or fertig == "y":
            datasheetwriter()
            print("Dokument erfolgreich erzeugt!")
            print("Enter drücken um das Programm zu schließen! \nBis dann :)")
            input("")
    elif fertig=="N" or fertig == "n":
        print("Dokument erfolgreich erzeugt!")
        datasheetwriter()
        berichtsheftmaschine9000()
    else:
        print("Falsche Eingabe!")
        datasheetwriter()
        fertigmachen()

def chooser():
    kliste = [1,2,3,4,5]
    kwert=[]
    kwert=random.choices(kliste,weights=(1,5,6,5,2),k=1)
    #print(str(kwert[0]))
    global aufgabenlisterandom
    aufgabenlisterandom=[]
    aufgabenlisterandom=(random.sample(presets,kwert[0]))

def tagwahl():
    global Datum1,Datum2,tagdt,tagwahleins
    tagwahleins=False
    Datum1 = input("Von welchem Tag aus? (tt.mm): ")
    tagdt = datetime.datetime.strptime(Datum1, '%d.%m')
    tagdtneu = tagdt + datetime.timedelta(days=4)
    Datum2 = tagdtneu.strftime('%d.%m')


def berichtsheftmaschine9000():
    #Gespeicherte Daten einlesen
    with open("datasheet.txt") as data:
        global datalist
        inhalt=data.read()
        datalist=inhalt.split(', ')
        set(datalist)
        datalist=datalist[:-1]

    #Werte Verteilen Header
    global BNr,Name,Jahr,NameIch,wocheeins
    BNr=datalist[0]
    print("Berichtsheft Nr.: "+BNr)
    Name=datalist[1]
    Jahr=datalist[2]
    NameIch = (datalist[3])

    if tagwahleins!=False:
        tagwahl()
    else:
        neuerdatechooser()

    #############Wochentage bearbeiten################
    Aktivität=range(5)
    global presets
    presets=datalist[4::]
    wochenaktivitäten = []


    for Aktiv in range(len(Aktivität)):
        chooser()
        x = len(aufgabenlisterandom)   # 3
        for aufgabe in aufgabenlisterandom:
            wochenaktivitäten.append(aufgabe)
        while x < 5:
            wochenaktivitäten.append(" ")
            x=x+1
            #print("Filler: "+str(x))



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
        global tagwahleins
        tagwahleins=True
        berichtsheftmaschine9000()

checkdatasheet()






###Matthias Fuchs 19.05.2021###


