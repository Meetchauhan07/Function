#Question 1
def count_lower_upper(str1):
    dict1={"UpperCase":0, "LowerCase":0}
    for i in str1:
        if i.isupper():
            dict1["UpperCase"]+=1
        elif i.islower():
            dict1["LowerCase"]+=1
    
    return dict1
    
sample_string=input("Enter a string: ")
print(f"Count of lowercase and uppercase letters is {count_lower_upper(sample_string)}")
'''
output:
Enter a string: MEetc
Count of lowercase and uppercase letters is {'UpperCase': 2, 'LowerCase': 3}
'''
#question 2
import math

def compute(n):
    return n+(n*10 + n)+(n*100 + n*10 + n)+(n*1000 + n*100 + n*10 + n)
for num in range(4,8):
    print(f"{num} = {compute(num)}")

'''
output:
4 = 4936
5 = 6170
6 = 7404
7 = 8638
'''
#Question 3
def createArray(r1,r2,r3,n):
    lst=[[[n for i in range(r1)] for j in range(r2)] for k in range(r3)]
    return lst
print(createArray(3,4,5,4))
'''
output:
[[[4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4]], [[4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4]], [[4, 4, 4], [4, 4, 4],
[4, 4, 4], [4, 4, 4]], [[4, 4, 4],
[4, 4, 4], [4, 4, 4], [4, 4, 4]], [[4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4]]]
'''




