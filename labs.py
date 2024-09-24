'''
There are 3 labs in the CSE department(L1, L2, and L3) with a seating capacity of x, y, and z respectively. Find the lab which has minimal seating capacity.  
Input format:
Input consists of 3 integers
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
Output format:
Print the minimal seating lab capacity
Refer the Sample output for formatting
Sample Input:
30
40
20
Sample Output:
L3
'''
l1=int(input())
l2=int(input())
l3=int(input())
if l1<l2 and l1<l3:
  print(l1)
elif l2<l1 and l2<l3:
  print(l2)
else:
  print(l3)
