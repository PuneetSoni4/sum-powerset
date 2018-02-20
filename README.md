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

Therefore, if S has n elements in it then, P(s) will have 2^n elements.

About the project
-----------------

The main goal behind this project is to "get the sum of all elements of power-set of numbers".

I have provided different solutions to this problem which are as follows:

**1. Using "itertools.combinations" library:**

  Using this library, the program generates all possible set combinations of given data to create it's power-set. After getting all elements of power-set, program simply sums all elements.
  
**2. Using "binary bits":**
  
  First of all the size of powerset is calculated with formula "2^n", where n = number of elements in S. After that, a counter loop is ran till the size of powerset with internal loop, looping over size of set. if internal loop's bit in the outer counter is set, then program captures that element from data list.
  
  Example: If S={"a","b","c"} then possible binary combinations for 3 strings will be 2^3 = 8, which are as follows:

          {000} -> {}

          {001} -> {c}

          {011} -> {bc}

          {010} -> {b}

          {100} -> {a}

          {101} -> {ac}

          {110} -> {ab}

          {111} -> {abc}

  Finally, when power-set is found, the program sums all elements of power-set.
  
**3. Using "Python Generators":**
  
  A python generator is created to generate power-set combinations.

**4. Using "Recursion":**

  A simple recursion method helps to generate power-set combinations.

**5. Using "Logic":**

  I tried creating my own logic to generate sum of power-set elements of given data. I was able to compute power-set sum, if the length of data string is lesser than or equal to four (4). 

How to run python test script file?
-----------------------------------

py.test test_sum_powerset.py

**PS: IMPORT APPROPRIATE LIBRARY BEFORE RUNNING TEST FILE.**

NOTE:
-----

If user passes elements of string as non-integers, the python script simply returns "-1".
