import random
import my_module

random_integer= random.randint(1, 10) 
 # Generates a random integer between 1 and 10 (inclusive)

print(random_integer)
print(my_module.my_favourite_number)
# output
# 9
# 3.1415


random_number_0_to_1 = random.random() 
print(random_number_0_to_1)
# output
# 0.4136768175067467


random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)
# output
# 8.499122734115852



random_float = random.uniform(1, 10)
print(random_float)
# output
# 9.846181924726261




random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")