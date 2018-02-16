# sum-powerset

What is Power Set?
------------------

If S is the set {a, b, c}, then the subsets of S are

{} (the empty set or the null set)

{a}

{b}

{c}

{a, b}

{a, c}

{b, c}

{a, b, c}

and hence the power set of S is {{}, {a}, {b}, {c}, {a, b}, {a, c}, {b, c}, {a, b, c}}.

About the project
-----------------

The main goal behind this project is to "get the sum of all elements of power-set of numbers".

I have provided different solutions to this problem which are as follows:

1. Using "itertools.combinations" library:

  Using this library, the program generates all possible set combinations of given data to create it's power-set. After getting all elements of power-set, program simply sums all elements.
  
2. Using "binary bits":
  
  This is implemented by considering each element of data as binary bit and then, program does left shift to generate different binary combinations. These combinations are then used to generate power-set.
  
  Example: If S={"a","b","c"} then possible binary combinations for 3 strings will be 2^3 = 8, which are as follows:

          {000} -> {}

          {001} -> {c}

          {011} -> {bc}

          {010} -> {b}

          {100} -> {a}

          {101} -> {ac}

          {110} -> {ab}

          {111} -> {abc}

  Finally, when power-set is found, simply summing all elements of power-set.
  
3. Using "Python Generators":
  
  A recursive python generator is created to generate power-set combinations.

4. Using "Logic":

  I am trying to create my own logic to generate power-set elements of given data. So far, I am able to compute power-set sum, if the length of data string is lesser than or equal to four (4). 
  
  Currenctly I am working on modifying and enhancing this logic using recursion to generate power-set for any data length.

How to run python test script file?
-----------------------------------

py.test test_sum_powerset.py

**PS: IMPORT APPROPRIATE LIBRARY BEFORE RUNNING TEST FILE.**

NOTE:
-----

If user passes elements of string as non-integers, the python script simply returns "-1".
