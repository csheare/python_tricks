# Idiom 1: use enumerate instead of creating an index

my_fruits = ['Apple', 'Pear', 'Banana']

for index, fruit in enumerate(my_fruits):
	print(f'{index}, {fruit}')

# Idiom 2: Use the in keyword to iterate over an iterable

for fruit in my_fruits:
	print(fruit)

# Idiom 3: Use else to execute code after a for loop concludes

my_friends = [('Madision', 22),('Alyssa', 26), ('Debby', 68 )]

for friend in my_friends:
	print(friend)
	if friend[1] > 65:
		print("old gal pal")
		break
else:
	print("you are a hip young lady, Courtney Shearer")

