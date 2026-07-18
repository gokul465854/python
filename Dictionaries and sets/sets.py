# -------creation of set-----
my_sets = {1,2,3,4,5,6}

# using the set() constructor
# print(my_sets)

# empty set
my_sets = set()

# -----set operation------
# 1: adding element
# my_sets.add('javascript')
# print(my_sets)

# my_sets = set(['java','python', 'html', 'css'])
# my_sets.remove('javascript')
# print(my_sets)


# issubset() and issuperset() fuctions

my_set = {1,2,3,4,5}
your_set = {2,3,4,6}

print(your_set.issubset(my_set))
print(my_set.issuperset(your_set))

# The .isdisjoint() method checks if two sets are disjoint, which means they don't have any elements in common. In this case, that's False because my_set and your_set do have common elements – 2, 3, and 4:
print(my_set.isdisjoint(your_set))

# he union operator | returns a new set with all the elements from both sets:
print(my_set | your_set) # {1, 2, 3, 4, 5, 6}

# The intersection operator & returns a new set with only the elements that the sets have in common:
print(my_set & your_set) #{2, 3, 4}

# The difference operator - returns a new set with the elements of the first set that are not in the other sets. In this example, the numbers 1 and 5 are in my_set but NOT in your_set:
print(my_set - your_set) # {1, 5}

# The symmetric difference operator ^ returns a new set with the elements that are either in the first or the second set, but not both. In this case, 1 and 5 are in my_set but not in your_set, so they are included. And the number 6 is in your_set but not in my_set, so it's included as well:
print(my_set ^ your_set) # {1, 5, 6}

print(5 in my_set)