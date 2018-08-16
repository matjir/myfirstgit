age=25
point=0
print("Valkommen till spelet")

question=input("Hur manga fragor vill du svara pa (1 eller 2)? ")
fraga=input("Hur gammal ar Matilda? ")

question=int(question)
fraga = int(fraga)

if question==2:
    if fraga == age:
        point = point+1
        print("Det var ratt.Du har " + str(point) + " poang")
        fraga2= input("Vart bor Matilda? ")

        if fraga2 == "uppsala":
            point = point + 1
            print("Du var ratt. Spelet ar slut och du har " + str(point) + " poang")
        else:
            print("Det var fel. Spelet ar slut och du har " + str(point) + " poang")

    else:
        print("Det var fel. Spelet ar slut och du har " + str(point) + " poang")


elif fraga != age:
        print("Det var fel. Spelet ar slut och du har " + str(point)+ " poang")



else:
    point=point+1
    print ("Det var rätt. Spelet ar slut och du har " + str(point)+ " poang")