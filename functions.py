# def test_recipe(food1,food2):
#     return "The great taste of " + food1 + " and " + food2
#
# food1="lasanga"
# food2="pasta"
#
# foodnames = test_recipe(food1,food2)
#
# print(foodnames)

def dec_to_cup(antal_dec):

    return (antal_dec)/2.37

deciliter= int(input("Hur många deciliter vill du dricka idag? "))

print("Du kommer dricka " + str(dec_to_cup(deciliter)) + " koppar idag.")




