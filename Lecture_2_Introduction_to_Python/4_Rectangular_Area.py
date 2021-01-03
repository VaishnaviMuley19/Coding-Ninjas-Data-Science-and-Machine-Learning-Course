""" You are given a rectangle in a plane. The corner coordinates of this rectangle is provided to you. You have to print the amount of area of the plane covered by this rectangles.
The end coordinates are provided as four integral values: x1, y1, x2, y2. It is given that x1 < x2 and y1 < y2.
Sample Input:
1
1
3
3
Sample Output:
4
"""

x1 = int(input())

y1 = int(input())

x2 = int(input())

y2 = int(input())

area = (x2-x1)*(y2-y1)

print(area)
