"""
Count Vowels - Enter a string and the program counts the number
of vowels in the text. For added complexity have it report a sum
of each vowel found.
"""

s = input('Enter a string:\n').lower()
vowels = list("aeiou")
count = {}
for c in s:
    if c in vowels:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1

print(count)
