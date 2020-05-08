money = int(input())

farm_animals = {"chicken": 23,
                "goat": 678,
                "pig": 1296,
                "cow": 3848,
                "sheep": 6768}
chart = dict()
tempA = 0  # Temporary number for amount of animals
exp_animal = "None"  # Most expensive animal

# Creating new Dict() that has animals name and amount of animals can be bought
for animal, cost in farm_animals.items():
    if money >= cost:  # Have enough money
        chart[animal] = money // cost
    else:
        chart[animal] = 0
        print(chart)

for animal, value in chart.items():
    if value > tempA:
        tempA = value
        exp_animal = animal

if tempA == 0:
    print(exp_animal)
elif tempA == 1:
    print(str(tempA) + ' ' + exp_animal)
else:
    if exp_animal == 'sheep':
        print(str(tempA) + ' ' + exp_animal)
    else:
        print(str(tempA) + ' ' + exp_animal + 's')
