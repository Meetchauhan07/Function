#Question 7
def is_palindrome(str1):
    if(str1==str1[::-1]):
        return True
    else:
        return False
    # return str1, str1[::-1]
    
string1=input("Enter a string: ")
if is_palindrome(string1):
    print(f"{string1} is palindrome")
else:
    print(f"{string1} is not palindrome")
'''
output:
Enter a string: eme
eme is palindrome
'''

#Question 8
def convert(str1):
    str1=str1.lower()
    words_list=str1.split()
    words_list=' '.join(sorted(list(set(words_list))))
    return words_list

string1=input("Enter a string: ")
print(f"Formatted string is: {convert(string1)}")
'''
output:
Enter a string: Meet
Formatted string is: meet
'''

#Question 9
def count_alpha_digits(str1):
    alpha_num_count={'alphabets':0, 'numbers':0}

    for i in str1:
        if i.isalpha():
            alpha_num_count['alphabets']+=1
        elif i.isdigit():
            alpha_num_count['numbers']+=1
    
    return alpha_num_count

string1=input("Enter a string: ")
print(f"The number of alphabets and digits in string is: {count_alpha_digits(string1)}")
'''
output:
Enter a string: hello
The number of alphabets and digits in string is: {'alphabets': 5, 'numbers': 0}
'''




