money = int(input())

farm_animals = {"chicken": 23,
                "goat": 678,
                "pig": 1296,
                "cow": 3848,
                "sheep": 6768}
chart = dict()
tempA = 0  # Temporary number for amount of animals
exp_animal = "None"  # Most expensive animal


def most_expensive(dic):
    temp_key = "Blank"
    temp_value = 0
    for key, val in dic.items():
        if val > temp_value:
            temp_value = val
            temp_key = key
    return temp_key, temp_value


last_animal = most_expensive(farm_animals)  # Output (animal, cost)

# Creating new Dict() that has animals name and amount of animals can be bought
for animal, cost in farm_animals.items():
    if money >= cost:  # Have enough money
        chart[animal] = money // cost

for animal, value in chart.items():
    if value < last_animal[1]:
        tempA = value
        exp_animal = animal


if tempA == 0:
    print(exp_animal)  # Prints None
elif tempA == 1:
    print(str(tempA) + ' ' + exp_animal)
else:
    if exp_animal == 'sheep':
        print(str(tempA) + ' ' + exp_animal)
    else:
        print(str(tempA) + ' ' + exp_animal + 's')
