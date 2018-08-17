# ##skriver ut namn, age, skill med en funktion
# def presentation(name,age,skill):
#     print("This is my name: "+ name + " and this is my age: " + age + " and this is my skill i'm undefeated in: " + skill)
#
# fraga1=input("Vad heter du? ")
# fraga2=input("Hur gammal är du? ")
# fraga3=input("Vad är din hemliga skill? ")
#
# presentation(fraga1,fraga2,fraga3)


# -----------------------------------------------------------------
###räknar ut tip baserat på kostnad med en funktion
# def tipmaker(pris):
#     if pris > 100:
#         tip=pris*0.1
#     else:
#         tip=pris*0.05
#     return tip
#
# import math
#
# prisfraga=float(input("Hur mycket kostade din måltid? ange i kronor: "))
#
# print("Du bör betala " + (str(round(tipmaker(prisfraga),2))) + " kr i tip")

#----------------------------------------------------------------------------------------------------------------------
##skriver ut ett statement beroende på random nummer
# fortune=["You are the best!", "You're rocking!", "How awsome you're today!", "Hi there cooling!"]
#
# import random
# randomnumber=random.randint(0,3)
# print("Your fortune cookie is telling you: " + str(fortune[randomnumber]))
# -------------------------------------------------------------------------------------------------------
##skriver ut nummer mellan två siffror
# fraga1=int(input("Vilket är ditt startnummer?: "))
# fraga2=int(input("Vilket är ditt slutnummer?: "))
# nylista=[]
# for i in range(fraga1,fraga2+1):
# #     nylista[i-fraga1]=fraga1+1
# # print("Här är alla siffror mellan dessa tal: " + [nylista])
#     print(i)
# ---------------------------------------------------------------------------------------
#gör ett ord baklänges och med stora bokstäver
# fraga1=input("Skriv ett ord: ")
#
# nylista=[]
#
# for i in range(0,len(fraga1)):
#     split=fraga1[-1-i]
#     nylista.append(split)
#
# str1 = ''.join(nylista)   #join gör om en lista till en string
# bigletter=str1.upper()
# print(bigletter)
# --------------------------------------------------------------------------------------------------------
#gör ett ord baklänges och med stora bokstäver
# fraga1=input("Skriv ett ord: ")
#
# nylista=""
#
# for i in range(0,len(fraga1)):
#     split=fraga1[-1-i]
#     nylista += (split)  #nylista är en string där split läggs till
#
# bigletter=nylista.upper()
# print(bigletter)
#
# -----------------------------------------------------------------------------------------------------------
##Gör om språk till rövarspråk
print("Hej, i detta program översätts ord till rövarspråket")
fraga1=input("Skriv ett ord: ")

nylista=[]  #ny lista
nylista1=[]

for i in range((len(fraga1))):  #ger nummer från noll till hur många bokstäver ordet är
    split=fraga1[0+i]                 #tar ut första bokstaven från ordet
    nylista.append(split)   #lista med varje bokstav på varje plats
    print(nylista)

for j in range(len(nylista)):
    if not (nylista[j] == "a" or "o" or "u" or "å" or "e" or "i" or "y" or "ä" or "ö"):
        #nylista1.insert(j, 30)
        nylista1.insert(j, (nylista[j] + "o" +nylista[j])) #HÄR är det knas!!!
        print(nylista1)
        # to_str= "".join(nylista)
        # print(to_str)

