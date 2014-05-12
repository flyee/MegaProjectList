"""
Check if Palindrome - Checks if the string entered by the user
is a palindrome. That is that it reads the same forwards as
backwards like “racecar”
"""

s = input("Input a string:\n").lower()

isPalindrome = True

for i in range(len(s)//2):
    if s[i] != s[len(s)-1-i]:
        isPalindrome = False
        break

if isPalindrome:
    print("\"%s\" is a palindrome." % s)
else:
    print("\"%s\" is not a palindrome." % s)
