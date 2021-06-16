from stories import madlib_1, madlib_2, madlib_3


import random

story = ["story 1", "story 2", "story 3"]
a = ["A", "a"]
b = ["B", "b"]
c = ["C", "c"]
d = ["D", "d"]

print("Choose a Madlib")
print("A = Going to the Zoo")
print("B = At the Arcade")
print("C = Disney Land Trip")
print("D = Random out of above (may get repeats)")

user_choice = input()

if user_choice in a:
    madlib_1()
elif user_choice in b:
    madlib_2()
elif user_choice in c:
    madlib_3()

def random_madlib():
    if user_choice in d:
	    return random.choice(story)
    else:
        pass

if random_madlib() == story[0]:
    madlib_1() 
elif random_madlib() == story[1]:
    madlib_2()
elif random_madlib() == story[2]:
    madlib_3() 
