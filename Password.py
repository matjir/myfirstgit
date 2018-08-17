import random

tal=list(range(0,100))
adjektiv=["rod", "blå", "snäll","rolig", "mjuk", "hög"]
substantiv=["bil", "dator", "människa", "soffa", "fluga"]
skiljetecken=[".",",",":","_","-",";","!"]
lista=[adjektiv,substantiv,skiljetecken,tal] #sätter alla andra listor i en lista

def test(nuk):
    randomnummer = random.randint(0, (len(nuk)-1)) #ger ett random
    return nuk[randomnummer] # ger tillbaka ett ord/tecken från en av listorna i listan

fraga=input("Vill du ha ett helt random lösenord? svara ja eller nej ")

while fraga != "nej":
    password = ""

    for k in range(0,len(lista)):
        ord=test(lista[k])
        password= str(ord) + str(password)


    print("Här är ett säkert lösenord till dig: " + password)
    fraga=input("Vill du ha ett nytt lösenord? ja eller nej: " )
