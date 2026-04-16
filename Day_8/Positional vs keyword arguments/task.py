
#postional arguments

def greet_with(name, location):
    print(f"Hello, {name}!")
    print(f"What is it like in {location}?")


greet_with("Bob", "New York")

#keyword arguments
greet_with(location="Los Angeles", name="Charlie")

