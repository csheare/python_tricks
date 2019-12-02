# zip example
# calls iter() on each of its arguments, then advances each iterator with next() and aggregates the results into tuples using their corresponding elements


print('Zip Example: list(zip([1, 2, 3], [a, b, c]))')

print(list(zip([1, 2, 3], ['a', 'b', 'c'])))


# map

print('Map Example: list(map(len,[abc,de,fghi]))')

print(list(map(len, ['abc','de','fghi'])))

# could combine: list(map(sum, zip([1, 2, 3], [4, 5, 6])))

# really cool example of grouping with iterables!!

inputs = [1,2,3,4,5,6,7,8,9,10]

def grouper(nums,n):
    '''
    nums: list of elements
    n: length of lists to divide nums into
    '''
    # first, create a list of references to the
    # same iterator
    iters = [iter(nums)] * n
    # second, return a list of tuples of size n
    # this works because for each iter in iters
    # the next() method is called, but since they
    # are pointing to the same object, n elements
    # are iterated over in the iter object as a time
    return zip(*iters)

