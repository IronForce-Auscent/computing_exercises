# What is this?
This is a series of programs aimed at demonstrating the 7 basic time complexities in the Big-O notation

## What is the Big-O notation/time complexity?

It is a fundemental tool used by computer scientists to gauge the cost of an algorithm, using (basic?) algebraic terms
(read: estimates the runtime of a program)

Wikipedia's definition of Big-O notation:
> Big O notation is a mathematical notation that describes the limiting behavior of a function when the argument tends towards a particular value or infinity. It is a member of a family of notations invented by Paul Bachmann, Edmund Landau, and others, collectively called Bachmann–Landau notation or asymptotic notation.

## The 7 time complexities (ranked from best to worst)
- (O(1))[o_1.py] time complexity: your code will take the same amount of time to execute every time regardless of input size 
    - Example: accessing the first item of a non-empty array
- O(log n) time complexity: your code's runtime increases logarithmically (Google/ChatGPT this if you dont know what it means) relative to the input size 
    - Example: binary search algorithms
- O(n) time complexity: your code's runtime increases proportionally to the input size
    - Example: looping through an array to find an item
- O(n log n) time complexity: your code's runtime increases proportionally to _n_ multiplied by the logarithm of _n_
    - Example: merge sort and quicksort algorithms
- O(n ^ 2) time complexity: your code's runtime increases quadratically relative to the input size
    - Example: nested FOR loops that checks each item in an array with another array

    > Sample psuedocode:
    ```
    for item_x in array_x:
        for item_y in array_y:
            if item_x is equal to item_y, print "Found a matching pair!"
            else, continue looping through each item in array_y
    ```
- O(2 ^ n) time complexity: your code's runtime increases exponentially relative to input size
    - Example: brute-forcing the Travelling Salesman problem, trying every possible route between cities

- O(n!) time complexity: your code's runtime increases factorially relative to input size (read: your code probably runs as fast as a sloth can run)
    - Example: brute-forcing the Travelling Salesman probelm, trying every possible permutation between cities


### <b>Note about the two Travelling Salesman Problems (TSP):</b> 
The TSP mentioned in the O(2 ^ n) example tests for every possible subset of cities to visit in order to visit each one, which allows for repeat visits to 1 or more cities

The TSP mentioned in the O(n!) example tests for every possible permutation of cities to visit in order to visit each one, which prevents the program from visiting any city more than once
