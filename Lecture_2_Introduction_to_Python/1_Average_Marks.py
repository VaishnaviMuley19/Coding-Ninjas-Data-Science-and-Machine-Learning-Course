""" Write a program to input marks of three tests of a student (all integers). Then calculate and print the average of all test marks.
Input format :
3 Test marks (in different lines)

Output format :
Average 

Sample Input 1 :
3 
4 
6

Sample Output 1 :
4.333333333333333

Sample Input 2 :
5 
10 
5

Sample Output 2 :
6.666666666666667
"""

# Read input as sepcified in the question
# Print output as specified in the question
marks_1 = int(input())
marks_2 = int(input())
marks_3 = int(input())

average = (marks_1 + marks_2 + marks_3)/3
print(average)
