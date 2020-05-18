pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"


def message(dish_name):
    return "You can make {}".format(dish_name)


def str_to_lis(string):
    return string.split(', ')


def check_ingredients(recipe, ingredient):
    if ingredient in recipe:
        return True
    else:
        return False


ingred = input()
cookbook = {'pasta': str_to_lis(pasta),
            'apple_pie': str_to_lis(apple_pie),
            'ratatouille': str_to_lis(ratatouille),
            'chocolate_cake': str_to_lis(chocolate_cake),
            'omelette': str_to_lis(omelette)}

for dish_name, recipe in cookbook.items():


print(cookbook)
print(message('pasta'))
print(str_to_lis(pasta))
print(check_ingredients(pasta, "sal"))
print(check_ingredients(str_to_lis(pasta), "sat"))
