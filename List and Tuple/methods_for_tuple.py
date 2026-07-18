
programing_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(programing_languages.count('python'))

print(programing_languages.index('Java'))

print(programing_languages.index('Python', 2, 5))

numbers = (13,2,78,3,45,67,18,7)
print(sorted(numbers))

print(sorted(programing_languages,key=len))

print(sorted(programing_languages,reverse=True))
