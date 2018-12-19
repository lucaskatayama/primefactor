## Problem A
A prime number p≥2 is an integer which is evenly divisible by only two integers: 1 and p. A composite integer is one which is not prime. The fundamental theorem of arithmetic says that any integer x can be expressed uniquely as a set of prime factors – those prime numbers which, when multiplied together, give x. Consider the prime factorization of the following numbers:
```
10=2×516=2×2×2×2231=3×7×11
```

Consider the following process, which we’ll call prime reduction. Given an input x:
```
if x is prime, print x and stop
factor x into its prime factors p1,p2,…,pk
let x=p1+p2+⋯+pk
go back to step 1

```


Write a program that implements prime reduction.

### Input

Input consists of a sequence of up to 20000 integers, one per line, in the range 2 to 109. The number 4 will not be included in the sequence (try it to see why it’s excluded). Input ends with a line containing only the number 4.

### Output
For each integer, print the value produced by prime reduction executed on that input, followed by the number of times the first line of the process executed.


```text
Sample Input 1	Sample Output 1
2               2 1               
3               3 1
5               5 1               
76              23 2              
100             5 5             
2001            5 6            
4
```


## Running


To tun
```bash
$ time python -m cProfile primedata.py < sample1.in
```
