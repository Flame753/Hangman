pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"


def message(dish):
    return "You can make {}".format(dish)


def str_to_lis(string):
    return string.split(', ')


ingredient = input()
cookbook = {'pasta': str_to_lis(pasta),
            'apple pie': str_to_lis(apple_pie),
            'ratatouille': str_to_lis(ratatouille),
            'chocolate cake': str_to_lis(chocolate_cake),
            'omelette': str_to_lis(omelette)}

for dish_name, recipe_list in cookbook.items():
    if ingredient in recipe_list:
        print(message(dish_name))


