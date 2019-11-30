### Notes on Iterators
#### See: https://dbader.org/blog/python-iterators
- Objects with __iter__ and __next__ defined dunder methods automatically work with for-in loops

```
numbers = [1,2,3]
for n in numbers:
print(n)
```

- Iterators use excpetions to structure control flow. To signal the end of iteration, a Python iterator simply raises the built-in StopIteration exception.

#### Example Iterator Class
```
class BoundedRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value

```

- Class-based Iterators are only one way to write iterable objects in Python. Also consider generators and generator expressions.

### Notes on Generators
#### See: https://realpython.com/introduction-to-python-generators/
- generator functions are a "lazy iterator"
- lazy iterators do not store their contents in memory

#### Memory Errors
- Whole file is loaded into memory  when csv_reader is called! ahh!
```
def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result
```

### Generators
#### See: https://realpython.com/introduction-to-python-generators/

#### No Memory Errors
- this version opens the files, iterate through it, and yields a row, instead of returning the whole file.
- using yield will result in a generator object
```
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row
```

#### Generator Comprehension
- make sure to use () not [] !
```
csv_gen = (row for row in open(file_name))
```

#### Aside:
```
>>> import sys
>>> nums_squared_lc = [i * 2 for i in range(10000)]
>>> sys.getsizeof(nums_squared_lc)
87624
>>> nums_squared_gc = (i ** 2 for i in range(10000))
>>> print(sys.getsizeof(nums_squared_gc))
120
```

#### .send
- allows you to send a value back to the generator
- normally you would see yield used as a statememnt, but here it is an expression
- when execution pikcs up after yield, i will take the value that is sent
- this creates a coroutine!
```
def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = (yield num)
            if i is not None:
                num = i
        num += 1
        
pal_gen = infinite_palindromes()
for i in pal_gen:
    digits = len(str(i))
    pal_gen.send(10 ** (digits))
```

#### .throw
- allows you to throw exceptions with the generator

```
pal_gen = infinite_palindromes()
for i in pal_gen:
    print(i)
    digits = len(str(i))
    if digits == 5:
        pal_gen.throw(ValueError("We don't like large palindromes"))
    pal_gen.send(10 ** (digits))
```

#### .close()
- allows you to stop a generator

```
pal_gen = infinite_palindromes()
for i in pal_gen:
    print(i)
    digits = len(str(i))
    if digits == 5:
        pal_gen.close()
    pal_gen.send(10 ** (digits))

```


