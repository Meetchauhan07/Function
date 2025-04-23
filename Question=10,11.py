#Question 10
import operator

def frequency(str1):
    words_list=str1.split()
    freq_list={} 
    for i in words_list:
        if i not in freq_list:
            freq_list[i]=1
        else:
            freq_list[i]+=1
    
    freq_list=sorted(freq_list.items())
    return freq_list

string1=input("Enter a string: ") # Example: apple banana orange apple mango banana
print(f"Frequency of words in string is: {frequency(string1)}")
'''
output:
Enter a string: mango apple mango
Frequency of words in string is: [('apple', 1), ('mango', 2)]
'''
#Question 11
def create_list(lst1,lst2):
    return list(set(lst1) & set(lst2))

list1=[8,15,89,56,2]
list2=[46,59,89,2,39]
print(f"Intersection of both the list is: {create_list(list1,list2)}")
'''
output:
Intersection of both the list is: [89, 2]
'''

