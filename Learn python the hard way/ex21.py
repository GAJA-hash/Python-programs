def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions")

age = add(25, 5)
height = subtract(78, 18)
weight = multiply(100, 2)
iq = divide(100, 2)

print(f" Age = {age}, Height = {height}, Weight = {weight}, IQ = {iq}")

#A puzzle for the extra credit, type it anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print("That becomes:", what, "Can you do it by hand?")

#Study Drill
print(f" Age = {age}, Height = {height}, Weight = {weight}, IQ = {iq}")


age += (height + weight / iq)
print("Age now:", age)


start = iq + weight * age / iq * iq  #Ans is 6050.0 :)

print("start:", start)
