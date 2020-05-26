#Palindrome
word = 'hannah'
p = bool (word.find(word[::-1])+1)

#Sum of Even Numbers
n = 10
s = sum((range(n+1))[::2])

#Read lines of file into a list 
f = "myflie.txt"
lines = [line.strip() for line in open(f)]

#Factorial
from functools import reduce
n = 10
factorial = reduce(lambda x, y : x*y,\range(1, n+1))

#Fibonacci 
fib = lambda n: n if n <=1 else \ fib (n-1) + fib (n-2)
result = fib(10)

#Unzip 
z=[(1,2), (3,4), (5,6), (7,8)]
unzip = lambda z: list(zip(*z))
unzip(z)

#Get first and last element of list
l = [1,2,3,4]
first, *x, last = l

#PowerSet
from functools import reduce
data {1,2,3,4}
f = lambda l: reduce(lambda z,x: z + \ [y +[x] for y in z], l, [[]])
f(data)

#Reverse a String
a = "String to be Reversed"
print(l=a[::-1])