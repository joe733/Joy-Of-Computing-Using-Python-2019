'''
Given a matrix with N rows and M columns, the task is to check if the matrix is a Binary Matrix. A binary matrix is a matrix in which all the elements are either 0 or 1.

>>Input Format:
The first line of the input contains two integer number N and M which represents the number of rows and the number of columns respectively, separated by a space.
From the second line, take N lines input with each line containing M integer elements with each element separated by a space. 

>>Output Format:
Print 'YES' or 'NO' accordingly

>>Example:
Input:
3 3
1 0 0
0 0 1
1 1 0
Output:
YES 
'''
x, y = map(int, input().split())
z = [list(map(int, input().split())) for i in range(x)]
print("YES" if all(all(j<=1 for j in i) for i in z) else "NO", end="")
