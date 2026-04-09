# Priting 

print("hello world")
print("Hello vivek!\nHello world!\nHow are you?")
# run and its print hello world in terminal


#String Manipulation
print("Hello world!"+" "+"vivek")

#Inputs
print("Hello" + input("What is you name?")+"!")

#Variables
name ="jack"

print(name)

name="hello"

print(name)

#print(len(input("what is your name?")))

username=(input("Enter your username"))
length=len(username)
print(length)


#Variable Naming
#We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice. Write 3 lines of code to switch the contents of the variables. You are not allowed to type the words "milk" or "juice". You are only allowed to use variables to solve this exercise.

glass1 = "milk"
glass2 = "juice"
 
temp = glass1
glass1 = glass2
glass2 = temp



#Band Name Generator Project
print("Welcome to the Band Name Generator")
city = input("Which city did you grow up in?\n")
pet=input("What is the name of a pet?\n")
print("your Band name could be: " + city +" "+ pet)