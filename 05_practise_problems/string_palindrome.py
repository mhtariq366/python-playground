"""
palindrome of string. Ignoring lower and upper case senstivity.
"""


var = input("Enter word to check: ")

var_len = len(var)
var = ''.join(var.split()).lower()

palin = 1
for i in range(var_len):
    if var[i] != var[var_len-i-1]:
        palin = 0

if palin:
    print('its a palindrome')
else:
    print('not a palindrome')
