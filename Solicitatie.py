from os import name


print("""-------------------------------------------------------------
|   Solicitatie Circusdirecteur voor Circus HotelDeBotel    |
-------------------------------------------------------------""")
naam = input("Hoe heet u? ")

print("Top! dan gaan we nu beginnen " + naam + ".")

gender = input("Bent u een man of een vrouw? Beantwoord met M/F ")
if gender == ("M"):
    snor = int(input("Heeft U een snor? zo ja, hoe breed is die dan? geef antwoord in volle cm. "))
    if snor > (10):
        print("Top")
    else:
        print("Sorry maar het is helaas verplicht om het breeder dan dat te hebben.")
if gender == ("F"):
    krulhaar = input("heeft u krullend haar? ")
    if krulhaar == ("Ja"):
        rood = input("wat voor kleur is het? ")
        if rood == ("Rood"):
            lengte = int(input("hoe lang is het in cm? "))
            if lengte > (20):
                print("Top")
            elif lengte < (20):
                print("Sorry maar het moet langer zijn dan dat.")
        else:
            print("Sorry maar het moet rood zijn")        
    elif krulhaar == ("Nee"):
        print("Sorry maat het is verplicht om krullend haar te hebben")

if gender ==("M") and snor > (10) or gender ==("F") and krulhaar == ("Ja") and lengte > (20):
    lengtepersoon = int(input("Hoe lang bent u? antwoord in cm "))
    if lengtepersoon > (150):
        print("Top")
    elif lengte <= (150):
        print("Sorry maar dat is niet lang genoeg")

if lengtepersoon > (150):
    gewicht = int(input("Hoeveel kg weegt u? "))
    if gewicht > (90):
        print("Top")
    elif gewicht <= (90):
        print("Sorry maar dat is te licht")

if gewicht > (90):
    bezit = input("Bent u in bezit van een Diploma MBO-4 ondernemen, een geldig Vrachtwagen rijbewijs en een hoge hoed? Beanwtwoord met Ja of Nee ")
    if bezit ==("Ja"):
        print("Top")
    elif bezit ==("Nee"):
        print("Sorry maar die heb je allemaal nodig")

if bezit ==("Ja"):
    DierenPraktijk = int(input("Heeft u ervaring met dieren-dressuur? zo ja, hoeveel jaar? "))
    Jongleren = int(input("Heeft u jongleer ervaring? zo ja, hoeveel jaar? "))
    AcrobatiekPraktijk = int(input("Heeft u Acrobatiek ervaring? zo ja, hoeveel jaar? "))

if DierenPraktijk > (4) or Jongleren > (5) or AcrobatiekPraktijk > (3):
    print ("Top")
else:
    print("Sorry maar je hebt dan te weinig ervaring")

if DierenPraktijk > (4) or Jongleren > (5) or AcrobatiekPraktijk > (3):        #Eerste nutteloze vraag
    huisdieren = input("Heeft u huisdieren? ")
    if huisdieren ==("Ja"):
        print("Top")
    elif huisdieren ==("Nee"):
        print("Jammer")

if DierenPraktijk > (4) or Jongleren > (5) or AcrobatiekPraktijk > (3):        #Tweede nutteloze vraag
    hoogtevrees = input("Heeft u hoogte vrees? ")
    if hoogtevrees ==("Ja"):
        print("Jammer")
    elif hoogtevrees ==("Nee"):
        print("Top")

if DierenPraktijk > (4) or Jongleren > (5) or AcrobatiekPraktijk > (3):        #Derde nutteloze vraag
    DroomBaan = input("Is dit uw droom baan? ")
    if DroomBaan ==("Ja"):
        print("Top")
    elif DroomBaan ==("Nee"):
        print("Jammer")

if DierenPraktijk > (4) or Jongleren > (5) or AcrobatiekPraktijk > (3):        #Vierde nutteloze vraag
    AndereBaan = input("Is dit uw enige baan? ")
    if AndereBaan ==("Ja"):
        print("Jammer")
    elif AndereBaan ==("Nee"):
        print("Top")

if DierenPraktijk > (4) or Jongleren > (5) or AcrobatiekPraktijk > (3):
    Certificaat = input("Heeft u een Overleven met gevaarlijk personeel cvertificaat? ")
    if Certificaat ==("Ja"):
        print("Geweldig dat is het einde van de solicitatie. Je bent aangenomen " + naam + "!")
    elif Certificaat ==("Nee"):
        print("Helaas is dat verplicht, volgende keer beter")
        
