#Question 12
def prime_factors(num, factors=[],i=2):
    if num<=1:
            return factors
    elif num%i==0:
        factors.append(i)
        return prime_factors(num/i,factors,i)
    else:
        return prime_factors(num,factors,i+1)
n=int(input("Enter a number: "))
print(f"Prime factors of given number are: {prime_factors(n)}")

'''
output:
Enter a number: 86
Prime factors of given number are: [2, 43]
'''

#Question 13
def dec_to_bin(num):
    if num == 0:
        return ""  
    return dec_to_bin(num // 2) + str(num % 2)

print(dec_to_bin(189))

'''
output:
10111101
'''

#Question 14
def count_vowels(string1, count=0, i=0):
    vowels="aeiouAEIOU"
    if i==len(string1):
        return count
    elif string1[i] in vowels:
        return count + 1 + count_vowels(string1,count,i+1)
    else:
        return count_vowels(string1,count,i+1)

str1=input("Enter a string: ")
print(f"Number of vowels in the string are: {count_vowels(str1)}")

'''
output:
Enter a string: Dwij
Number of vowels in the string are: 1
'''



