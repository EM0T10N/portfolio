import random
# VERY IMPORTANT TO IMPORT RANDOM FIRST
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()[]{},;:.-_/\\?+*# "

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters

if lower:
    all += lowercase_letters

if nums:
    all += digits

if syms:
    all += symbols

length = 20
# LENGTH OF PASSWORD GENERATED
amount = 10
# AMOUNT OF PASSWORDS GENERATED

for x in range(amount):
    password = "".join(random.sample(all, length))
    #join function takes all items in an iterable and joins them into one string.
    print(password)
