cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = drivers * space_in_a_car
average_passengers_per_car = passengers / drivers
remaining_cars = cars - drivers
required_drivers = remaining_cars


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty dars today.")
print("We can transport", carpool_capacity, "passengers today.")
print("We have", passengers, "passengers to carpool today")
print('We need to put about', average_passengers_per_car, 'in each car.')
print('There are', remaining_cars, 'cars remaining')




crow = 4
hen = 5
cow = 6
goat = 3
print('Total birds', crow + hen)
print ('Total animals', cow + goat)


i = 4985
j = 8379
print('The modulus of 8379 and 4985 is', i % j, "\n And difference is", j - i )
