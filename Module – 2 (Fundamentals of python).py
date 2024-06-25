#!/usr/bin/env python
# coding: utf-8

# In[23]:


num = int(input("Enter a number: "))
if num > 0:
    print("The entered number is positive.")
elif num == 0:
    print("The entered number is zero.")
else:
    print("The entered number is negative.")


# In[24]:


from math import factorial
factorial(2)


# In[29]:


N=int(input("enter the number"))

if N%2==0:
    print("number is even")
else:
    print("number is  odd")


# In[56]:


character = input("Enter a character: ")  
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']  
  
if character in vowels:  
    print(f"The character '{character}' is a vowel!")  
else:  
    print(f"The character '{character}' is a consonant!")  


# In[58]:


X= int( input("Please enter value for X: "))  
Y = int( input("Please enter value for Y: "))  
   
temp_1 = X
X=Y  
Y = temp_1  
   
print ("The Value of X after swapping: ", X)  
print ("The Value of Y after swapping: ", Y)  


# In[69]:


def sum_three(x, y, z):
    if x == y or y == z or x == z:
        sum = 0
    else:
        sum = x + y + z
    return sum
print(sum_three(2, 1, 2))
print(sum_three(3, 2, 2))
print(sum_three(2, 2, 2))
print(sum_three(1, 2, 3))


# In[70]:


def test_number5(x, y):
    if x == y or abs(x - y) == 5 or (x + y) == 5:
        return True
    else:
        return False
print(test_number5(7, 2))
print(test_number5(3, 2))
print(test_number5(2, 2))
print(test_number5(7, 3))
print(test_number5(27, 53))


# In[71]:


n = int(input("Input a number: "))
sum_num = (n * (n + 1)) / 2
print("Sum of the first", n, "positive integers:", sum_num)


# In[73]:


def string_length(str1):
    count = 0
    for char in str1:
        count += 1
        return count
print(string_length('a')) 


# In[74]:


def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    
    return dict

print(char_frequency('a')) 


# In[75]:


def chars_mix_up(a, b):
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))


# In[76]:


def add_string(str1):
    length = len(str1)
    if length > 2:
        if str1[-3:] == 'ing':
            str1 += 'ly'
        else:
            str1 += 'ing'

    return str1

print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))


# In[78]:


def not_poor(str1):
    snot = str1.find('not')
    spoor = str1.find('poor')
    if spoor > snot and snot > 0 and spoor > 0:
        str1 = str1.replace(str1[snot:(spoor+4)], 'good')
        return str1
    else:
        return str1
print(not_poor('Ankit is not poor!'))
print(not_poor('Ankit is poor!'))


# In[ ]:




