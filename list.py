
quest=input("What do you like to do? ")
inventory=[]

while quest != 'stop':
	inventory.append(quest)
	quest = input("What do you like to do? ")

#inventory.remove("stop")
#for i in inventory:
	print("(Okay. I understand that your hobbies are {}".format(quest(i)))
