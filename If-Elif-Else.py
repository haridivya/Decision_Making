#decision_making_statments(if-elif-else)
'''
Write a program to check whether the given character is vowel or consonant.
Input format:
The input consist of a character
Output format:
The output consists of a below-given string
“Vowel” / “Consonant” / “Not an alphabet”
Sample Input:
e
Sample Output:
Vowel
'''
element=input()
vowels=['a','e','i','o','u','A','E','I','O','U']
if element.isalpha():
    if element in vowels:
        print("Vowel")
    else:
        print('Consonant')
else:
    print('Not an alphabet')
