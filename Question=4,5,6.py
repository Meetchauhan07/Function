#Question 4
def sum_avg(sub1,sub2,sub3,sub4,sub5):
    total=sub1+sub2+sub3+sub4+sub5
    average=total/5
    return total,average

Maths=int(input("Enter the marks of Maths: "))
Phy=int(input("Enter the marks of Physics: "))
Chem=int(input("Enter the marks of Chemistry: "))
PCo=int(input("Enter the marks of English: "))
Comp=int(input("Enter the marks of Computer: "))
total,average=sum_avg(Maths,Phy,Chem,PCo,Comp)
print(f"Your total is: {total}\nYour average is: {average}")
'''
output:
Enter the marks of Maths: 95
Enter the marks of Physics: 80
Enter the marks of Chemistry: 90
Enter the marks of English: 76
Enter the marks of Computer: 95
Your total is: 436
Your average is: 87.2
'''
#Question 5
def ispangram(str1):
    str1=str1.upper()
    str1=set(str1)
    checkstr={chr(i) for i in range(65,91)}
    if(checkstr.issubset(str1)):
        return True
    else:
        return False
string1="Crazy Fredrick bought many very exquisite opal jewels"
if(ispangram(string1)):
    print(f"{string1} is pangram")
else:
    print(f"{string1} is not pangram")
'''
output:
Crazy Fredrick bought many very exquisite opal jewels is pangram
'''
#Question 6
def squares_cubes(n):
    return [(i,i**2,i**3) for i in range(n+1)]

num=int(input("Enter a number: "))
print(f"Series of till given number is: {squares_cubes(5)}")
'''
output:
Enter a number: 89
Series of till given number is: [(0, 0, 0), (1, 1, 1),
(2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125)]
'''
























