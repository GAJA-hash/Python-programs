#Assigning two variables
def cheese_and_crackers(cheese_count, boxes_of_crackers):

    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")



print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10+20, 5+6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)


#Study Drill.
input("Let's do Study Drill")
def Animals(a1,a2,a3,a4,a5,a6): #numbers alone can't make the function name. So used a1
    print(f"first prize goes to {a1}.")
    print(f"2 prize goes to {a2}.")
    print(f"3 prize goes to {a3}.")
    print(f"4 prize goes to {a4}.")
    print(f"5 prize goes to {a5}.")
    print(f"6 prize goes to {a6}.")

b2 = "Zebra"
b1 = input("Enter 1th animal:" )
b4 = input("Enter 4th animal:")
Animals(b1, b2, input("Enter 3rd animal:"), f"{b4}", 'Hyena','fox')
