""" You are given first three entries of an arithmetic progression. You have to calculate the common difference and print it.
Sample Input:
1
3
5
Sample Output:
2
"""

# Write your code here
a = int(input())
b = int(input())
c = int(input())

diff1 = c - b
diff2 = b - a
if diff1 == diff2:
    print(diff1)
