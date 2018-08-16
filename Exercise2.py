# def presentation(name,age,skill):
#     print("This is my name: "+ name + " and this is my age: " + age + " and this is my skill i'm undefeated in: " + skill)
#
# fraga1=input("Vad heter du? ")
# fraga2=input("Hur gammal är du? ")
# fraga3=input("Vad är din hemliga skill? ")
#
# presentation(fraga1,fraga2,fraga3)



def tipmaker(pris):
    if pris > 100:
        tip=pris*0.1
    else:
        tip=pris*0.05
    return tip
import math
prisfraga=float(input("Hur mycket kostade din måltid? ange i kronor: "))

print("Du bör betala " + (str(round(tipmaker(prisfraga),2))) + " kr i tip")