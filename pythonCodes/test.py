random = [10,5, 9, 'cat']
# converting the list to an iterator
random_iterator = iter(random)
print(random_iterator)
print(next(random_iterator))
print(next(random_iterator))
print(next(random_iterator))

# Python code to demonstrate the working of
# zip()

# initializing lists
name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]
marks = [ 40, 50, 60, 70 ]

# using zip() to map values
mapped = zip(name, roll_no, marks)
print(mapped)
# converting values to print as set otherwise it's not printable
mapped = set(mapped)  # or list()

# printing resultant values
print ("The zipped result is : ",end="")
print (mapped)

players = [ "Sachin", "Sehwag", "Gambhir", "Dravid", "Raina" ]
print("hehe")
# initializing their scores
scores = [100, 15, 17, 28, 43 ]
print(*zip(players, scores))
dict_test = dict(zip(players, scores))
print(dict_test)
print(type(dict_test))
print("hehe")
for pl, sc in zip(players, scores):
    print(f"Player : {pl} Score: {sc}")
for pl, sc in dict_test.items():
    print(f"Player : {pl}  Score : {sc}")
# printing players and scores.
# for pl, sc in zip(players, scores):
lst = ['am', 'watermelon', 'girl', 'boy', 'colour']
print(enumerate(lst))
print('hehe43')
for x,y in enumerate(lst):
    print(x)
    print(x,y)
    print(y)
print('hehe48')
for x in enumerate(lst):
    print(x)

def palindromeD(c):
    c_inv = ""
    # for i in range(len(c)):
    #         c_inv = c[i] + c_inv
    for i in range(-1,-len(c)-1,-1):
            c_inv = c[i] + c_inv
    print(c_inv)
    return c == c_inv

palindromeD("test")

def count_vowels(in_string):
    """ Returns the number of vowels contained in `in_string`"""
    num_vowels = 0
    vowels = "aeiouAEIOU"

    for char in in_string:
        if char in vowels:
            num_vowels += 1  # equivalent to num_vowels = num_vowels + 1
    return num_vowels

print(count_vowels.__doc__)

