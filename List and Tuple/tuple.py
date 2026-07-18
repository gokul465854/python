# programing_languages = ['python','Java', 'C++']
# print(programing_languages.index('Javas'))


developer = ('Alice', 34, 'Python Developer', 'New York')
# print(developer[-2])

text = 'Hello, World!'
# print(tuple(text))

programing = ('python',45, 'Java', 'C++')
# print('Java' in programing)
# print('javascipt' in programing)
# name,age,job = developer
# print(name + ' is a ' + job + ' and is ' + str(age) + ' years old.')

name,*rest = developer
# print(name)
# print(rest)

# print(developer[1:3])

del developer[3]
print(developer)