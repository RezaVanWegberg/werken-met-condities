Question = input("Is de kaas geel? ")
if Question == ("ja"):
    Question0 = input("Zitter er gaten in? ")
    if Question0 == ("ja"):
        Question1 = input("Is de kaas belachelijk duur? ")
        if Question1 == ("ja"):
            print("Emmenthaler")
        elif Question1 == ("nee"):
            print("Leerdammer")
    elif Question0 == ("nee"):
        Question2 = input("Is de kaas hard als steen? ")
        if Question2 == ("ja"):
            print("Pamnigiano Reggiano")
        elif Question2 == ("nee"):
            print("Goudse kaas")
if Question == ("nee"):
    Question3 = input("Heeft de kaas blauwe schimmels? ")
    if Question3 == ("ja"):
        Question4 = input("Heeft de kaas een korst? ")
        if Question4 == ("ja"):
            print("Bleu de Rochbaron")
        elif Question4 == ("nee"):
            print("Foume d'Ambert")
    elif Question3 == ("nee"):
        Question5 = input("Heeft de kaas een korst?")
        if Question5 == ("ja"):
            print("Camembert")
        elif Question5 == ("nee"):
            print("Mozzarella")
