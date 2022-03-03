"""
Given a number n as input, print the following output. Use recursion. Do not use loops. Do a dry run for each test case.
Input-> 3
Output-> 3:Hello 2:Hello 1:Hello
"""

def recur(n):
  print(str(n)+":"+"Hello")
  if (n>1):
    recur(n-1)

num = 3
recur(num)