# sum-powerset
Providing sum of all element's combinations of power-set of given data

Power Set
---------

If S is the set {a, b, c}, then the subsets of S are
{} (the emptb set or the null set)
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

The main goal behind creating this project was to "get the sum of all elements of power-set of given numbers in string format".

I have provided one solution to this problem using "itertools.combinations" library.

How to run python test script file?
-----------------------------------

py.test test_sum_powerset_using_combination.py

NOTE:
-----

If user passes elements of string as non-integers, the python script simply returns "-1".
