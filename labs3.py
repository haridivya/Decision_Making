
'''
There are 3 labs in the CSE department are L1, L2, and L3 with a seating capacity of x, y, and z respectively. One of the 3 labs has been allocated for ACE training. Out of the available labs, find the lab which has minimal seating capacity.
Input format:
Input consists of 3 integers and a string
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
The fourth input denotes the lab which is allocated for ACE training
Output format:
Print the minimal seating capacity lab amongst the available labs.
Refer the Sample output for formatting
Sample Input:
30
40
20
L3
Sample Output:
L1
'''
l1=int(input())
l2=int(input())
l3=int(input())
val=input()
if 'l1'==val:
    if l2<l3:
        print(l2)
    else:
        print(l3)
elif 'l2'==val:
    if l1<l3:
        print(l1)
    else:
        print(l3)
elif 'l3' == val:
    if l1<l2:
        print(l1)
    else:
        print(l2)
else:
    print('invalid')

