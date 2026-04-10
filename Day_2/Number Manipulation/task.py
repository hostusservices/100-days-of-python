#Number Manipulation

#calculate bmi
#formula weight/height(square)

height=1.65
weight=84

bmi = weight/height**2


print(bmi) # showing in decimal

print(int(bmi)) #whole number

print(round(bmi)) #roundup the value

print (round(bmi,2)) # with 2 decimals

#outputs 
#30.85399449035813
#30
#31
#30.85

score = 0
height =1.8
is_winning=True
#user scores a point

score += 1
print(score)
score -= 1
print(score)
score *= 1
print(score)

#output
# 1
# 0
# 0

#f-strings
print(f"Your score is = {score},your height is {height}. You are Wining{is_winning}")
#Your score is = 0,your height is 1.8. You are WiningTrue

a = int("5") / int(2.7)

print(type(a))