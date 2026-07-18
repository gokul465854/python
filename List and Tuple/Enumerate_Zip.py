
# Enumerate is a built-in function in Python that allows you to loop through an iterable (like a list) and have an automatic counter. It returns both the index and the value of each item in the iterable.

languages = ['Marathi', 'Hindi', 'Gujarati', 'Telugu']

index = 1
for language in languages:
    print(f"Index {index} and language  {language}")
    index += 1
    
print(list(enumerate(languages)))

for index, laguage in enumerate(languages,1):
  print(f"Index {index} and language {laguage}")

# Zip is a built-in function in Python that allows you to combine two or more iterables (like lists) into a single iterable of tuples. Each tuple contains one element from each of the input iterables.

developer = ['Jai', 'Kundan','Chandan', 'Gokul']
ids = [1,2,3,4]
result = list(zip(developer, ids))
print(result)

# And here's an example of using the zip() function with a for loop to iterate over developers and ids:

developer = ['Jai', 'Kundan','Chandan', 'Gokul']
ids = [1,2,3,4]

for name, id in zip(developer, ids):
  print(f"Developer: {name}, Id: {id}")