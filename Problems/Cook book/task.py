pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"


def message(dish_name):
    return "You can make {}".format(dish_name)


def string_to_list(string):
    return string.split(', ')


def check_ingredients(recipe, ingredient):
    if ingredient in recipe:
        return True
    else:
        return False


print(message('pasta'))
print(string_to_list(pasta))
print(check_ingredients(pasta, "sal"))
print(check_ingredients(string_to_list(pasta), "sat"))
