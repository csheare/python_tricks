# Idiom 1: Prefer the format function for formating strings

name = "Courtney"
fav_food = "Maple Glazed Salmon Bites"

print('{0}s fav food is {1}'.format(name, fav_food))

# Idiom 2: Use ''.join when creating a single string for a list

my_name = ['Courtney', 'Ann', 'Shearer']
full_name = ' '.join(my_name)

assert( full_name == 'Courtney Ann Shearer')

# Idiom 3: Chain string functions to make a simple series of transformations more clear

book = 'The Soul of Man Under Socialism: Oscar Wilde'
no_author = book.strip(': Oscar Wilde')

assert(no_author == 'The Soul of Man Under Socialism')

all_upper = book.upper()

assert(all_upper == 'THE SOUL OF MAN UNDER SOCIALISM: OSCAR WILDE')

replace_colon = book.replace(':', ' by')

assert(replace_colon == 'The Soul of Man Under Socialism by Oscar Wilde')

all_change = book.strip().upper().replace(':', ' by')
assert(all_change == 'THE SOUL OF MAN UNDER SOCIALISM by OSCAR WILDE')

