

# # pizza = {
#   'name': 'Margherita pizza',
#   'price': 8.9,
#   'calories_per_slice': 250 ,
#   'toppings': ['mozzarella', 'basil']
# }
# for n in pizza:
#   print(n + ' ')

# print(pizza.get('name',[]))

# print(pizza.items())

# print(pizza.keys())
# print(pizza.values())

# print(pizza.items())

# pizza.clear()
# print(pizza.items())

# .pop() --
# pizza.pop('price',10)
# print(pizza.items())

# print(pizza.popitem())
# print(pizza.items())
pizza = dict([('name', 'Margherita pizza'), ('price',10), ('calaries_per_slice', 250), ('toppings', ['mozzerelia', 'basil'])])

pizza.update({'price': 15, 'price': 25})
print(pizza.items())