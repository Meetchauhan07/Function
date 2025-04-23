#Question 15
def rev_list(list1, x):
    if x==0:
        return list1
    return rev_list(list1[:])

print(rev_list([1,2,3,4,5],len([1,2,3,4,5])-1))

'''
output:

'''
#Question 16
def power(a,b):
    if b==0:
        return 1
    return a * power(a,b-1)

num=float(input("Enter a number: "))
raiseto=int(input("Enter the power to which you want to find the value: "))
print(f"Value of given number is {power(num,raiseto)}")

'''
output:

'''
#Question 17
def replace_negatives(list1, i=0):
    if i==len(list1):
        return list1
    elif list1[i]<0:
        list1[i]=0
        return replace_negatives(list1, i+1)
    else:
        return replace_negatives(list1, i+1)
print(f"Updated list is: {replace_negatives([-2,-1,-3,0,1,2,3,4,5])}")

'''
output:

'''
