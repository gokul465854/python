# loops - A loop is a programming construct that allows you to repeat a block of code multiple times. In Python, there are two main types of loops: for loops and while loops.

programing_languages = ['Rust', 'Java','Python', 'C++']
for language in programing_languages:
  print(language)


for char in 'code':
  print(char)

categories = ['Fruits', 'Vegetables']
foods = ['Apple', 'Carrot', 'Banana']

for category in categories:
  for food in foods:
    # print(category, food)

# while loop - A while loop is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition. The loop will continue to execute as long as the condition remains true. Once the condition becomes false, the loop will terminate and the program will continue with the next statement after the loop.
    secret_number = 3
    guess = 0

while guess != secret_number:
      guess = int(input('Guess the number (1-5): '))
      if guess != secret_number:
         print('Wrong guess. Try again!')
print('Congratulations! You guessed the number.')

developer_names = ['jess', 'Naomi','Tom']

for developer in developer_names:
  if developer == 'Naomi':
    continue
  print(developer)

words = ['Sky', 'apple', 'rhythm', 'fly', 'orange']
 
# nested Loop - A nested loop is a loop that is contained within another loop. The inner loop will be executed for each iteration of the outer loop. Nested loops are often used to iterate over multi-dimensional data structures, such as lists of lists or matrices.
for word in words:
  for letter in word:
    if letter.lower() in 'aeiou':
      print(f"{word} contains the vowel '{letter}'")
      break
  else:
    print(f"'{word}' has no vowels")