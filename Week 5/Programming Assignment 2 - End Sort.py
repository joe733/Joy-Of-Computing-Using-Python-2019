'''
Given a list A of N distinct integer numbers, you can sort the list by moving an element to the end of the list. Find the minimum number of moves required to sort the list using this method in ascending order. 

>>Input Format:
The first line of the input contains N distinct integers of list A separated by a space.

>>Output Format
Print the minimum number of moves required to sort the elements.

>>Example:

Input:
1 3 2 4 5

Output:
3

>>Explanation:
In the first move, we move 3 to the end of the list. In the second move, we move 4 to the end of the list, and finally, in the third movement, we move 5 to the end. 
'''
x = list(map(int, input().split()))
y = x.copy()
x.sort()
k = 0
for i,j in zip(x, x[1:]):
    if x == y:
        break
    if y.index(i) > y.index(j) and i<j:
        y.append(y.pop(y.index(j)))
        k+=1
print(k,end="")
