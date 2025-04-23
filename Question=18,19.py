#Question 18
def average(list1, i=0, count=0, sum=0):
    if i==len(list1):
        return sum/count
    else:
        return average(list1,i+1,count+1,sum+list1[i])
    
print(average([1,2,3,4,5]))
'''
output:
3.0


'''
#Question 19
def length_string(str1):
    if str1=="":  
        return 0
    else:
        return 1+length_string(str1[1:])  

print(length_string("Apple"))
'''
output:
5

'''
