#
# Exploring Arguments and Parameters
#####################################
#
# Familiar Functions
#####################################
print("\n############## Familiar Functions ##############\n ")
def print_two(a, b):
    print("Arguments: {0} and {1}".format(a, b))

# print_two() #invalid
print_two(4, 1)
# print_two(41) #invalid
# print_two(a=4, 1) #invalid
# print_two(4, a=1) #invalid
# print_two(4, 1, 1) #invalid
# print_two(b=4, 1) #invalid
print_two(a=4, b=1)
print_two(b=1, a=4)
# print_two(1, a=1) #invalid
# print_two(4, 1, b=1) #invalid
print("\n############## Default Arguments ##############\n")
#
# Default Arguments
#####################################

def keyword_args(a, b=1, c='X', d=None):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)

keyword_args(5)
print("\n")
keyword_args(a=5)
print("\n")
keyword_args(5, 8)
print("\n")
keyword_args(5, 2, c=4)
print("\n")
keyword_args(5, 0, 1)
print("\n")
keyword_args(5, 2, d=8, c=4)
print("\n")
# keyword_args(5, 2, 0, 1, "") #invalid - TypeError: for passing 5 args
# keyword_args(c=7, 1) # invalid - non keyword arg after keyword arg 
keyword_args(c=7, a=1)
print("\n")
keyword_args(5, 2, [], 5)
print("\n")
# keyword_args(1, 7, e=6) #invalid - TypeError: keyword_args() got multiple values for argument 'e'
keyword_args(1, c=7)
# keyword_args(5, 2, b=4) #invalid - TypeError: keyword_args() got multiple values for argument 'b'

print("\n##############  Exploring Variadic Argument lists ##############\n")

#
# Exploring Variadic Argument lists
#####################################

def variadic(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

variadic(2, 3, 5, 7)
print("\n")
variadic(1, 1, n=1)
print("\n")
# variadic(n=1, 2, 3) # invalid - non keyword arg
variadic()
print("\n")
variadic(cs="Computer Science", pd="Product Design")
print("\n")
# variadic(cs="Computer Science", cs="CompSci", cs="CS") #invalid - keyword arg repeted
variadic(5, 8, k=1, swap=2)
print("\n")
variadic(8, *[3, 4, 5], k=1, **{'a':5, 'b':'x'})
print("\n")
# variadic(*[8, 3], *[4, 5], k=1, **{'a':5, 'b':'x'}) # invalid - invalid syntax
# variadic(*[3, 4, 5], 8, *(4, 1), k=1, **{'a':5, 'b':'x'}) # invalid - invalid syntax
variadic({'a':5, 'b':'x'}, *{'a':5, 'b':'x'}, **{'a':5, 'b':'x'})


print("\n##############  Optional: Putting it all together ##############\n")

#
# Optional: Putting it all together
#####################################

def all_together(x, y, z=1, *nums, indent=True, spaces=4, **options):
    print("x:", x)
    print("y:", y)
    print("z:", z)
    print("nums:", nums)
    print("indent:", indent)
    print("spaces:", spaces)
    print("options:", options)

# all_together(2) #invalid - TypeError: all_together() missing 1 required positional argument: 'y'
all_together(2, 5, 7, 8, indent=False)
print("\n")
all_together(2, 5, 7, 6, indent=None)
print("\n")
# all_together() #invalid - TypeError: all_together() missing 2 required positional arguments: 'x' and 'y'
# all_together(indent=True, 3, 4, 5) #invalid - non keyword arg
# all_together(**{'indent': False}, scope='maximum') #invalid - invalid syntax
all_together(dict(x=0, y=1), *range(10))
print("\n")
# all_together(**dict(x=0, y=1), *range(10)) #invalid - invalid syntax
# all_together(*range(10), **dict(x=0, y=1)) #invalid - TypeError: all_together() got multiple values for argument 'x'
all_together([1, 2], {3:4})
print("\n")
# all_together(8, 9, 10, *[2, 4, 6], x=7, spaces=0, **{'a':5, 'b':'x'}) #invalid - TypeError: all_together() got multiple values for argument 'x'
all_together(8, 9, 10, *[2, 4, 6], spaces=0, **{'a':[4,5], 'b':'x'})
print("\n")
# all_together(8, 9, *[2, 4, 6], *dict(z=1), spaces=0, **{'a':[4,5], 'b':'x'}) #invalid - invalid syntax


print("\n############## Writing Functions ##############\n##############  speak_excitedly ##############\n\n")

#
# speak_excitedly
#####################################

def speak_excitedly(message, numberOfExclamation=1, enthusiasm=False):
    message += '!' * numberOfExclamation
    if not enthusiasm:
        return message
    return message.upper()

print(speak_excitedly("I love Python"))
print("\n")
print(speak_excitedly("Keyword arguments are great", numberOfExclamation=4))
print("\n")
print(speak_excitedly("I guess Java is okay...", numberOfExclamation=0))
print("\n")
print(speak_excitedly("Let's go Stanford", numberOfExclamation=2, enthusiasm=True))

#
# average
#####################################

print("\n##############  Average ##############\n")

def average(*nums):
    if not nums: return None
    return sum(nums) / len(nums)

print(average())  # => None
print(average(5)) # => 5.0
print(average(6, 8, 9, 11))  # => 8.5

#
#Challenge:  make_table ##Too Hard
#####################################

print("\n##############  make_table ##############\n")

def make_table(key_justify = 'left', value_justify = 'right', **kwargs):
    
    justification = {
        'left': '<',
        'right': '>',
        'center': '^'
    }
    if key_justify not in justification or value_justify not in justification:
        print("Error! Invalid justification specifier.")
        return None

    key_alignment_specifier = justification[key_justify]
    value_alignment_specifier = justification[value_justify]

    max_key_length = max(map(len, kwargs.keys()))
    max_value_length = max(map(len, kwargs.values()))

    total_length = 2 + max_key_length + 3 + max_value_length + 2
    print('=' * total_length)
    for key, value in kwargs.items():
        print('| {:{key_align}{key_pad}} | {:{value_align}{value_pad}} |'.format(key, value,
            key_align=key_alignment_specifier, key_pad=max_key_length,
            value_align=value_alignment_specifier, value_pad=max_value_length
        ))
    print('=' * total_length)

make_table(
    first_name="Sam",
    last_name="Redmond",
    shirt_color="pink"
)

make_table(
    key_justify="right",
    value_justify="center",
    song="Style",
    artist_fullname="Taylor $wift",
    album="1989"
)


print("\n############## Function Nuances ##############\n##############  Return ##############\n\n")

#
# Return
#####################################

def say_hello():
    print("Hello!")

print(say_hello())  # => Hello! None


def echo(arg=None):
    print("arg:", arg)
    return arg

print(echo())  # => arg: None None
print(echo(5)) # => arg: 5 5
print(echo("Hello")) # => arg: Hello Hello

def drive(has_car):
    if not has_car:
        return
    return 100  # miles

print(drive(False))  # => None
print(drive(True))   # => 100

print("\n############## Parameters and Object Reference ##############\n")

#
# Parameters and Object Reference
#####################################

def reassign(arr):
    arr = [4, 1]
    print("Inside reassign: arr = {}".format(arr))

def append_one(arr):
    arr.append(1) 
    print("Inside append_one: arr = {}".format(arr))

l = [4]
print("Before reassign: arr={}".format(l))  # => Before reassign: arr=[4]
reassign(l)                                 # => Inside reassign: arr=[4,1]
print("After reassign: arr={}".format(l))   # => After reassign: arr=[4]
print("\n")
l = [4]
print("Before append_one: arr={}".format(l))  # => Before reassign: arr=[4]
append_one(l)                                 # => Inside reassign: arr=[4,1]
print("After append_one: arr={}".format(l))   # => After reassign: arr=[4,1]

#
# Scope
#####################################

print("\n############## Scope ##############\n")
print("\nCase 1\n")
# Case 1
x = 10

def foo():
    print("(inside foo) x:", x)
    y = 5
    print(' value:', x * y)

print("(outside foo) x:", x)
foo()
print("(after foo) x:", x)
print("\nCase 2\n")
# Case 2
x = 10

def foo():
    x = 8  # Only added this line - everything else is the same
    print("(inside foo) x:", x)
    y = 5
    print('value:', x * y)

print("(outside foo) x:", x)
foo()
print("(after foo) x:", x)

#
# Default Mutable Arguments - A Dangerous Game
#####################################

print("\n############## Default Mutable Arguments - A Dangerous Game ##############\n")

x = 5

def f(num=x):
    return num * num

x = 6
print(f())   # => 25, not 36
print(f(x))  # => 36
print("\n")

def append_twice(a, lst=[]):
    lst.append(a)
    lst.append(a)
    return lst
   
# Works well when the keyword is provided
print(append_twice(1, lst=[4]))  # => [4, 1, 1]
print(append_twice(11, lst=[2, 3, 5, 7]))  # => [2, 3, 5, 7, 11, 11]

# But what happens here?
print(append_twice(1))
print(append_twice(2))
print(append_twice(3))





