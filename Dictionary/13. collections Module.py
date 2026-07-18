# Problem with Normal Dictionary
dict = {}

# for ch in "banana":
#     dict[ch] += 1
# print(dict) -->  KeyError: 'b', because b key not present in th dictionary

# solution this problem --> defaultdict()

from collections import defaultdict
freq = defaultdict(int)
for ch in "banana":
    freq[ch] += 1

print(freq)
