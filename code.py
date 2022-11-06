//Define a function called myfunc that takes in an arbitrary number of arguments, and returns a list containing only those arguments that are even?
def myfunc(*args):
    return [n for n in args if n%2 == 0]

print(myfunc(1,2,3,4,5,6,7,8,9,10))
# [2, 4, 6, 8, 10]






