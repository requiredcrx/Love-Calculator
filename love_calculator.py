# Asking for name input
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is your partner's name? \n")


# counting the number of time true love occurs in the names

name_combined = name1 + name2
t = name_combined.lower().count("t")
r = name_combined.lower().count("r")
u = name_combined.lower().count("u")
e = name_combined.lower().count("e")

true = t + r + u  + e

l = name_combined.lower().count("l")
o = name_combined.lower().count("o")
v = name_combined.lower().count("v")
e = name_combined.lower().count("e")

love = l + o + v + e
name_count = str(true) + str(love)

Total = int(name_count)
print(Total) 
if Total < 10 or Total > 90:
    print(f"Your score is {Total}, you go together like coke and mentos.")
elif Total >= 40 and Total <= 50:
    print(f"Your score is {Total}, you are alright together.")
else:
    print(f"Your score is {Total}, fair enough.")
