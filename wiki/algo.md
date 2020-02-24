https://web.cs.dartmouth.edu/

## why pseudocode

We just described the binary search algorithm in English, stepping through one example. That's one way to do it, but a human language explanation can vary in quality. It can be too short or too long, and most importantly, it's not always as precise as it should be. We could jump to showing you binary search in a programming language like JavaScript or Python, but programs contain lots of details - due to requirements imposed by the programming language, or because programs have to handle errors caused by bad data, user error, or system faults - and those can make it hard to understand the underlying algorithm from studying just the code. That's why we prefer to describe algorithms in something called pseudocode, which mixes English with features that you see in programming languages.

## linear search
We know that linear search on an array of nnn elements might have to make as many as nnn guesses. You even might have perceived that the difference between the worst-case number of guesses for linear search and binary search becomes more striking as the array length increases. Let's see how to analyze the maximum number of guesses that binary search makes.

If we start with an array of length 8, then incorrect guesses reduce the size of the reasonable portion to 4, then 2, and then 1. Once the reasonable portion contains just one element, no further guesses occur; the guess for the 1-element portion is either correct or incorrect, and we're done. So with an array of length 8, binary search needs at most four guesses.

Let's look at the general case of an array of length nnn. We can express the number of guesses, in the worst case, as "the number of times we can repeatedly halve, starting at nnn, until we get the value 1, plus one." But that's inconvenient to write out.

![](../static/img/algo/2020-01-22-12-18-42.png)
![](../static/img/algo/2020-01-22-12-18-53.png)
![](../static/img/algo/2020-01-22-12-19-08.png)
![](../static/img/algo/2020-01-22-12-20-21.png)
![](../static/img/algo/2020-01-22-12-21-09.png)


### binary search

* initial version

Let min = 0 and max = n-1.
Compute guess as the average of max and min, rounded down (so that it is an integer).
If array[guess] equals target, then stop. You found it! Return guess.
If the guess was too low, that is, array[guess] < target, then set min = guess + 1.
Otherwise, the guess was too high. Set max = guess - 1.
Go back to step 2. (this looks like a loop)

* improved version to include not figuring in the array situation
https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/implementing-binary-search-of-an-array

Let min = 0 and max = n-1.
If max < min, then stop: target is not present in array. Return -1.
Compute guess as the average of max and min, rounded down (so that it is an integer).
If array[guess] equals target, then stop. You found it! Return guess.
If the guess was too low, that is, array[guess] < target, then set min = guess + 1.
Otherwise, the guess was too high. Set max = guess - 1.
Go back to step 2.

### cost example

alpha + number
the Tycho-2 star catalog contains information about the brightest 2,539,913 stars in our galaxy. Suppose that you want to search the catalog for a particular star, based on the star's name. If the program examined every star in the star catalog in order starting with the first, an algorithm called linear search, the computer might have to examine all 2,539,913 stars to find the star you were looking for, in the worst case.

If the catalog were sorted alphabetically by star names, binary search would not have to examine more than 22 stars, even in the worst case.


## binary searchguessing number

The computer is going to randomly select an integer from 1 to 15. You'll keep guessing numbers until you find the computer's number.

Maybe you guessed 1, then 2, then 3, then 4, and so on, until you guessed the right number. We call this approach linear search, because you guess all the numbers as if they were lined up in a row.

How about on average? If the computer is equally likely to select any number from 1 to 15, then on average you'll need 8 guesses.

Since the computer tells you whether a guess is too low, too high, or correct, you can start off by guessing 8. If the number that the computer selected is less than 8, then because you know that 8 is too high, you can eliminate all the numbers from 8 to 15 from further consideration. If the number selected by the computer is greater than 8, then you can eliminate 1 through 8. Either way, you can eliminate half the numbers.

We call this halving approach binary search, and no matter which number from 1 to 15 the computer has selected, you should be able to find the number in **at most** 4 guesses with this technique.


![](../static/img/algo/2020-01-22-12-05-42.png)

```javascript
var primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];
```

Suppose we want to know whether the number 67 is prime. If 67 is in the array, then it's prime.

Looking at the example below, we can read the array of prime numbers from left to right, one at a time, until we find the number 67 (in the pink box) and see that it is at array index 18. Looking through the numbers in order like this is a linear search.
![](../static/img/algo/2020-01-22-12-08-15.png)


## Route-finding

![](../static/img/algo/2020-01-22-11-57-55.png)
![](../static/img/algo/2020-01-22-12-01-49.png)

The algorithm needs to determine which of the surrounding squares are indeed "closer to the goal", and we can do that by assigning a "cost" to each square that represents the minimum number of steps the character would have to take to get from that vertex to the goal.

How is the current Prince William related to King William III, who endowed the College of William and Mary in 1693?
What path should a ghost follow to get to Pac-Man as quickly as possible?
What's the best way to drive from Dallas, Texas to Orlando, Florida?

the problem is to find a path along black squares that leads the ghost to Pac-Man

## asymptotic notation

So far, we analyzed linear search and binary search by counting the maximum number of guesses we need to make. But what we really want to know is how long these algorithms take. We're interested in **time**, not just **guesses**. The running times of linear search and binary search include the time needed to make and check guesses, but there's more to these algorithms.

### running time

The running time of an algorithm depends on how long it takes a computer to run the lines of code of the algorithm—and that depends on the speed of the computer, the programming language, and the compiler that translates the program from the programming language into code that runs directly on the computer, among other factors.

* First, we need to determine how long the algorithm takes, in terms of the size of its input.

Or think about a GPS. If it knew about only the interstate highway system, and not about every little road, it should be able to find routes more quickly, right? So we think about the running time of the algorithm as a function of the size of its input.

* rate of growth

![](../static/img/algo/2020-01-22-12-29-46.png)
![](../static/img/algo/2020-01-22-12-30-59.png)

By dropping the less significant terms and the constant coefficients, we can focus on the important part of an algorithm's running time—its rate of growth—without getting mired in details that complicate our understanding. When we drop the constant coefficients and the less significant terms, we use asymptotic notation.

![](../static/img/algo/2020-01-22-12-32-38.png)

```javascript
var doLinearSearch = function(array, targetValue) {
  for (var guess = 0; guess < array.length; guess++) {
    if (array[guess] === targetValue) {
        return guess;  // found it!
    }
  }
  return -1;  // didn't find it
};
```

![](../static/img/algo/2020-01-22-12-42-56.png)

![](../static/img/algo/2020-01-22-12-43-28.png)

![](../static/img/algo/2020-01-22-12-43-56.png)

When we use big-Θ notation, we're saying that we have an asymptotically tight bound on the running time. "Asymptotically" because it matters for only large values of nnn. "Tight bound" because we've nailed the running time to within a constant factor above and below.

### big o notation
![](../static/img/algo/2020-01-22-12-56-23.png)

We use big-Θ notation to asymptotically bound the growth of a running time to within constant factors above and below. Sometimes we want to bound from only above.


![](../static/img/algo/2020-01-22-13-00-49.png)

![](../static/img/algo/2020-01-22-12-54-59.png)
![](../static/img/algo/2020-01-22-13-01-54.png)

We use big-O notation for asymptotic upper bounds, since it bounds the growth of the running time from above for large enough input sizes.  worst is big o, the exact running time is very possibly under

![](../static/img/algo/2020-01-22-13-03-02.png)
![](../static/img/algo/2020-01-22-13-03-31.png)
![](../static/img/algo/2020-01-22-13-04-32.png)
![](../static/img/algo/2020-01-22-13-05-24.png)

### big omega notation

![](../static/img/algo/2020-01-22-13-06-40.png)

We use big-Ω notation for asymptotic lower bounds, since it bounds the growth of the running time from below for large enough input sizes.

Similarly, we can correctly but imprecisely say that the worst-case running time of binary search is Ω(1), left parenthesis, 1, right parenthesis, because we know that it takes at least constant time.


### big theta


![](../static/img/algo/2020-01-22-12-45-38.png)
be careful only log is the same not the exponential
![](../static/img/algo/2020-01-22-12-46-13.png)
![](../static/img/algo/2020-01-22-13-17-24.png)
![](../static/img/algo/2020-01-22-12-47-10.png)
![](../static/img/algo/2020-01-22-12-47-53.png)
![](../static/img/algo/2020-01-22-12-48-27.png)
see 8 for the note
![](../static/img/algo/2020-01-22-12-49-34.png)

### selection sort

[analysis](https://www.khanacademy.org/computing/computer-science/algorithms/sorting-algorithms/a/analysis-of-selection-sort)
There are many different ways to sort the cards. Here's a simple one,called selection sort, possibly similar to how you sorted the cards above:

Find the smallest card. Swap it with the first card.
Find the second-smallest card. Swap it with the second card.
Find the third-smallest card. Swap it with the third card.
Repeat finding the next-smallest card, and swapping it into the correct position until the array is sorted.

* Pascal cours1 reverse sort

![](../static/img/algo/2020-01-22-13-33-20.png)

It might be tricky to write code that found the index of the second-smallest value in an array. I'm sure you could do it, but there's a better way. Notice that since the smallest value has already been swapped into index 0, what we really want is to find the smallest value in the part of the array that starts at index 1. We call a section of an array a subarray, so that in this case, we want the index of the smallest value in the subarray that starts at index 1.

![](../static/img/algo/2020-01-22-13-36-55.png)

### insertion sort

![](../static/img/algo/2020-01-22-13-49-18.png)
[analysis of insertion sort](https://www.khanacademy.org/computing/computer-science/algorithms/insertion-sort/a/analysis-of-insertion-sort)

