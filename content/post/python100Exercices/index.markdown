---
title: 100 Best Python Exercises For Beginners 1-10 (30 minutes read)
summary: 1-10
subtitle: THE BEST IS YET TO COME
authors:
- Xiaoou WANG
tags: ["100 Python Exercises","Python"]
categories: ["Python Exercises","Python"]
date: "2020-02-25"
# lastMod: "2019-09-05T00:00:00Z"
featured: false
draft: false
markup: blackfriday
toc: true
# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: ""
  focal_point: ""

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references
#   `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
# projects: ["Python"]
---



{{< figure library="true" src="enjoy.png" lightbox="true" >}}


{{% toc %}}

[link to all the questions](https://hackmd.io/dcoNudOsS4eWwdEU0_Otqg?view#Question-9)

[link to the jupyter file](https://gist.github.com/xiaoouwang/b9845c3bce33eb5c9ec1df2939bd05a7)

## 1. Find all numbers divisible by 7 but not a multiple of 5, between 2000 and 3200 (both sides included).

{{% alert tip %}}
The numbers obtained should be printed in a comma-separated sequence on a single line.
{{% /alert %}}

> 4 solutions given here


```python
# 1. most intuitive way
for number in range(2000,3201):
        if (number%7 == 0) and (number%5 != 0):
            print(number,end = ",")
```

```
2002,2009,2016,2023,2037,2044,2051,2058,2072,2079,2086,2093,2107,2114,2121,2128,2142,2149,2156,2163,2177,2184,2191,2198,2212,2219,2226,2233,2247,2254,2261,2268,2282,2289,2296,2303,2317,2324,2331,2338,2352,2359,2366,2373,2387,2394,2401,2408,2422,2429,2436,2443,2457,2464,2471,2478,2492,2499,2506,2513,2527,2534,2541,2548,2562,2569,2576,2583,2597,2604,2611,2618,2632,2639,2646,2653,2667,2674,2681,2688,2702,2709,2716,2723,2737,2744,2751,2758,2772,2779,2786,2793,2807,2814,2821,2828,2842,2849,2856,2863,2877,2884,2891,2898,2912,2919,2926,2933,2947,2954,2961,2968,2982,2989,2996,3003,3017,3024,3031,3038,3052,3059,3066,3073,3087,3094,3101,3108,3122,3129,3136,3143,3157,3164,3171,3178,3192,3199,
```


```python
# 2. use list and join
l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        # str() very important coz join only work on strings
        l.append(str(i))
','.join(l)
```

```
'2002,2009,2016,2023,2037,2044,2051,2058,2072,2079,2086,2093,2107,2114,2121,2128,2142,2149,2156,2163,2177,2184,2191,2198,2212,2219,2226,2233,2247,2254,2261,2268,2282,2289,2296,2303,2317,2324,2331,2338,2352,2359,2366,2373,2387,2394,2401,2408,2422,2429,2436,2443,2457,2464,2471,2478,2492,2499,2506,2513,2527,2534,2541,2548,2562,2569,2576,2583,2597,2604,2611,2618,2632,2639,2646,2653,2667,2674,2681,2688,2702,2709,2716,2723,2737,2744,2751,2758,2772,2779,2786,2793,2807,2814,2821,2828,2842,2849,2856,2863,2877,2884,2891,2898,2912,2919,2926,2933,2947,2954,2961,2968,2982,2989,2996,3003,3017,3024,3031,3038,3052,3059,3066,3073,3087,3094,3101,3108,3122,3129,3136,3143,3157,3164,3171,3178,3192,3199'
```


```python
# 3. one liner see here for a very common caveat https://stackoverflow.com/questions/60379194/why-join-doesnt-work-on-a-list-comprehension
','.join([str(number) for number in range(2000,3201) if number%7 == 0 and number%5 != 0])
```

```
'2002,2009,2016,2023,2037,2044,2051,2058,2072,2079,2086,2093,2107,2114,2121,2128,2142,2149,2156,2163,2177,2184,2191,2198,2212,2219,2226,2233,2247,2254,2261,2268,2282,2289,2296,2303,2317,2324,2331,2338,2352,2359,2366,2373,2387,2394,2401,2408,2422,2429,2436,2443,2457,2464,2471,2478,2492,2499,2506,2513,2527,2534,2541,2548,2562,2569,2576,2583,2597,2604,2611,2618,2632,2639,2646,2653,2667,2674,2681,2688,2702,2709,2716,2723,2737,2744,2751,2758,2772,2779,2786,2793,2807,2814,2821,2828,2842,2849,2856,2863,2877,2884,2891,2898,2912,2919,2926,2933,2947,2954,2961,2968,2982,2989,2996,3003,3017,3024,3031,3038,3052,3059,3066,3073,3087,3094,3101,3108,3122,3129,3136,3143,3157,3164,3171,3178,3192,3199'
```


```python
# 4. use filter see https://www.geeksforgeeks.org/filter-in-python/
numbers = range(2000,3201)
result = filter(lambda x: x%7 == 0 and x%5 !=0, numbers)
print(list(result))
```

```
[2002, 2009, 2016, 2023, 2037, 2044, 2051, 2058, 2072, 2079, 2086, 2093, 2107, 2114, 2121, 2128, 2142, 2149, 2156, 2163, 2177, 2184, 2191, 2198, 2212, 2219, 2226, 2233, 2247, 2254, 2261, 2268, 2282, 2289, 2296, 2303, 2317, 2324, 2331, 2338, 2352, 2359, 2366, 2373, 2387, 2394, 2401, 2408, 2422, 2429, 2436, 2443, 2457, 2464, 2471, 2478, 2492, 2499, 2506, 2513, 2527, 2534, 2541, 2548, 2562, 2569, 2576, 2583, 2597, 2604, 2611, 2618, 2632, 2639, 2646, 2653, 2667, 2674, 2681, 2688, 2702, 2709, 2716, 2723, 2737, 2744, 2751, 2758, 2772, 2779, 2786, 2793, 2807, 2814, 2821, 2828, 2842, 2849, 2856, 2863, 2877, 2884, 2891, 2898, 2912, 2919, 2926, 2933, 2947, 2954, 2961, 2968, 2982, 2989, 2996, 3003, 3017, 3024, 3031, 3038, 3052, 3059, 3066, 3073, 3087, 3094, 3101, 3108, 3122, 3129, 3136, 3143, 3157, 3164, 3171, 3178, 3192, 3199]
```

## 2. Compute the factorial of a given numbers.

{{% alert tip %}}
Suppose the following input is supplied to the program:

8

Then, the output should be:

40320
{{% /alert %}}


```python
def factorial(number):
  # prevent some user input bug
  if number < 0:
    raise ValueError("No negative numbers please")
    # this is called the base case in recursion
  elif number == 0:
    return 1
  return number*factorial(number-1)
factorial(0)
```

```
1
```

for some nice introduction to recursion, see https://www.khanacademy.org/computing/computer-science/algorithms/recursive-algorithms/a/recursive-factorial

{{% alert success %}}
When we're computing n! in this way, we call the first case, where we immediately know the answer, **the base case**, and we call the second case, where we have to *compute the same function but on a different value*, **the recursive case**.
{{% /alert %}}

## 3. Compute power and use dictionary

With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.

{{% alert tip %}}
Suppose the following input is supplied to the program:

8

Then, the output should be:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
{{% /alert %}}


```python
def powerNumber(number):
    output = {} # or dict() if takes user input use int(input("please enter a number"))
    for i in range(1,number):
      output[i] = i*i
    return output
print(powerNumber(3))
```

```
{1: 1, 2: 4}
```

## 4. Convert comma separated string

Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number

{{% alert tip %}}
input: 34,67,55,33,12,98

output:

['34', '67', '55', '33', '12', '98']

('34', '67', '55', '33', '12', '98')

{{% /alert %}}


```python
L = "34,67,55,33,12,98".split(",") # the join syntax is with ".",join(L)
print(L)
```

```
['34', '67', '55', '33', '12', '98']
```

```python
print(tuple(L))
```

```
('34', '67', '55', '33', '12', '98')
```

## 5. Class and methods :
{{% alert tip %}}
getString: to get a string from console input.
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
{{% /alert %}}

```python
## the self parameter is a must, but not the others, see the setString method for a comparaison
class upper:
    def __init__(self):
        self.text = ""
    def getString(self):
        self.text = "test"
        # self.text = input("please type a string here")
    def upper(self):
        print(self.text.upper())
    def setString(self,newText):
        self.text = newText
test = upper()
test.getString()
test.upper()
```

```
TEST
```

```python
test.setString("hehe")
test.upper()
```

```
HEHE
```
{{% alert tip %}}

No new keyword to initiate an object, class is kind of like a function in Python

For more about class see https://www.geeksforgeeks.org/python-classes-and-objects/

`raw_input()` does not exist in Python 3.x, while `input()` does. Actually, the old raw_input() has been renamed to input()
{{% /alert %}}

## 6. Formula

{{% alert tip %}}
Q = Square root of [(2 * C * D)/H]

C is 50. H is 30.

D is the variable whose values should be input to your program in a comma-separated sequence.

Input:
100,150,180

Output:
18,22,24
{{% /alert %}}


```python
import math
c=50
h=30
value = []
# items = input("please enter comma separated numbers").split(',')
items = "100,150,180".split(',')
for d in items:
    # note the use of float() and str()
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
print(','.join(value))
```

```
18,22,24
```
## 7. 2-dimensional array

Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.

Note: i=0,1.., X-1; j=0,1..., Y-1.

{{% alert tip %}}
Input :
i = 3, j = 5

Then, the output of the program should be:

[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] =

first row = 0*(0|1|2|3|4)

second row = 1*(0|1|2|3|4)

{{% /alert %}}

```python
def toArray(row, col):
    multilist = [[0 for i in range(col)] for j in range(row)]
    for i in range(row):
        for j in range(col):
            multilist[i][j] = i * j
    print(multilist)
toArray(3, 5)
```

    [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

{{% alert success %}}
Explanation and some extra thinking https://spapas.github.io/2016/04/27/python-nested-list-comprehensions/
{{% /alert %}}

```python
# In fact [[0 for i in range(col)] for j in range(row)] = the following code
# first draw the column
hehehe = []
hehe = []
for col in range(x):
    hehe.append(0)
# then repeat the column to draw the whole array
for row in range(y):
    hehehe.append(hehe)
print(hehehe)
```




    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]




```python
# However the list comprehension normally takes the following form
non_flat = [ [1,2,3], [4,5,6], [7,8] ]
# the first for is the outer for, the next is the inner
print([y for x in non_flat for y in x])
for x in non_flat:
    for y in x:
        y
# see another example here
print([ y for x in non_flat if len(x) > 2 for y in x ])
# equals to
for x in non_flat:
    if len(x) > 2
        for y in x:
            y
# it's really important to see the last for as the innermost for
```




    [1, 2, 3, 4, 5, 6, 7, 8]
    [1, 2, 3, 4, 5, 6]




```python
# another somewhat complicate example, read from rightmost for = print all the letters and corresponding index for words of length > 2
strings = [ ['foo', 'bar'], ['baz', 'taz'], ['w', 'koko'] ]
[ (letter, idx) for idx, lst in enumerate(strings) for word in lst if len(word)>2 for letter in word]
```




    [('f', 0),
     ('o', 0),
     ('o', 0),
     ('b', 0),
     ('a', 0),
     ('r', 0),
     ('b', 1),
     ('a', 1),
     ('z', 1),
     ('t', 1),
     ('a', 1),
     ('z', 1),
     ('k', 2),
     ('o', 2),
     ('k', 2),
     ('o', 2)]

## 8. Sort a list

Take a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

{{% alert tip %}}

Input:
without,hello,bag,world

Output:
bag,hello,without,world

{{% /alert %}}

```python
words = "without,hello,bag,world".split(',')
# sorted(words) doesn't change words but return a new list, so it's better
print(sorted(words))
print(words)
# sort() returns None and changes the list in place
words.sort()
print(words)
```

    ['bag', 'hello', 'without', 'world']
    ['without', 'hello', 'bag', 'world']
    ['bag', 'hello', 'without', 'world']

{{% alert success %}}
`sorted(words)` doesn't change words but return a new list, so it's a better approach (no side effects), see `functional programming` in wikipedia (also compare with imperative programming and declarative programming). It's a problem of `Programming paradigm`.

https://www.wikiwand.com/en/Functional_programming

https://www.wikiwand.com/en/Side_effect_(computer_science)
{{% /alert %}}


## 9. Capitalization

Take a sequence of lines as input and prints the lines capitalized.

{{% alert tip %}}

Input:

Hello world

Practice makes perfect

Output:

HELLO WORLD

PRACTICE MAKES PERFECT
{{% /alert %}}


```python
lines = []
while True:
    s = input("put some lines here")
    if s:
        lines.append(s.upper())
    else:
        break;

for sentence in lines:
    print(sentence)
```

    put some lines heress
    put some lines heresss
    put some lines here
    SS
    SSS

{{% alert success %}}
Nothing complicated.

The interesting thing here is how to use `while` to keep asking inputs and `break` to stop the loop.
{{% /alert %}}


## 10. Remove duplicates

Take a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

{{% alert tip %}}
Input:
hello world and practice makes perfect and hello world again

output:
again and hello makes perfect practice world
{{% /alert %}}


```python
words = "hello world and practice makes perfect and hello world again"
wordsList = words.split(" ")
sorted(set(wordsList))
```




    ['again', 'and', 'hello', 'makes', 'perfect', 'practice', 'world']

{{% alert success %}}
The key thing here is to understand the difference between list and set (no duplicates in set).
{{% /alert %}}

{{< figure library="true" src="bravo.png" lightbox="true" >}}
