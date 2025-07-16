#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add(a,b):
    print("Sum is :", a+b)


add(1,2)


# In[7]:


def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
print("Factorial is : ", factorial(5))
        


# In[8]:


def simple_interset(principle, rate , time):
    print("Simple Interest is : " , (principle * rate * time)/100)


simple_interset(10000,10,2)


# In[11]:


def sum_of_natural_no(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    print(f"Sum of {n} natural number is : {sum}")

sum_of_natural_no(50)


# In[12]:


def table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

table(2)


# In[16]:


def odd_sum(n):
    sum = 0
    count = 0
    for i in range(1, n+1):
        if(i % 2 != 0):
            sum += i
            count += 1
    print("Sum : " , sum)
    print("Total odd number", count)

odd_sum(50)


# In[18]:


def square(n):
    print("Square", n ** n)

square(5)


# In[19]:


def add(a,b):
    print(a+b)
    def add1(c,d):
        print(c+d)

    
add1(c,d)
add(1,2)


# In[26]:


try:
    print(10/0)
except ZeroDivisionError:
    print("Hello")
finally :
    print("")



# In[48]:


def reverse(name):
    char = ""
    for i in range(len(name)-1,-1,-1) :
        char += name[i]
    return char
        


print(reverse("Python")) 


# In[ ]:


#test


# In[42]:


def square(n):
    print("Square", n * n)

square(6)


# In[43]:


def add(a,b):
    return a+b

a = add(1,2)
print(a)


# In[45]:


def even(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")


even(3)


# In[9]:


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

n = int(input("Enter a number"))
result = factorial(n)
print(result)


# In[ ]:


def fibo(n):
    num = int(input("Enter a number"))
    a = 0
    b = 1
    for i in range(0, num+1):
        print(a)
        c = a + b
        a = b 
        b = c




# In[53]:


def vowel_count(name):
    count = 0
    for i in name:
        if(i in ['a', 'e' ,'i', 'o' ,'u']):
            count += 1
    return count

a = vowel_count("Hello")
print(a)
    


# In[58]:


def sum(*args):
    result = 0
    for i in args:
        result += i
    return result

print(sum(1,2,3,4,5,6,7,8,9,10))


# In[72]:


def largest(l1):
    max = l1[0]
    for i in l1:
        if max < i:
            max = i
    return max

print(largest([1,2,3,4,5, 2000, 100]))


# In[64]:


def palindrome(name):
    char = ""
    for i in range(len(name)-1,-1,-1) :
        char += name[i]
    if name == char:
        print("Palindrome")
    else:
        print("Not a Palindrome")


palindrome("racecar")
palindrome("Hello")
        


# In[66]:


def fibbo(n):
    a = 0
    b = 1
    for i in range(0, n+1):
        print(a)
        c = a + b
        a = b 
        b = c

fibbo(12)


# In[67]:


print(type(lambda x: x))


# In[68]:


def foo(): pass

print(foo())


# In[69]:


print(len([1, 2, 3]))


# In[70]:


print(list(map(lambda x:x+1, [1,2,3])))


# In[71]:


print(bool('False'))


# In[78]:


def password():
    print("Hello I am your Assistant for tha Day")
    password = 1234
    attempt = 3
    while True:
        n = int(input("Enter your Password"))
        if n != password:
            attempt -= 1
            print("try again attempt left", attempt)
            
            if attempt == 0:
                print("Try again after some time")
                break
        else:
            print("Access Granted")
            break

password()

            


# In[1]:


def add(x, y=2):
    return x + y

print(add(3))


# In[5]:


#Write a function that takes two numbers and returns their average
def avg():
    a = int(input("Enter a number"))
    b = int(input("Enter second Number"))
    return (a+b)/2

a = avg()
print(a)


# In[6]:


def vowel_count():
    name = input("Enter a string")
    count = 0
    for i in name:
        if(i in ['a', 'e' ,'i', 'o' ,'u']):
            count += 1
    return count

a = vowel_count()
print(a)


# In[7]:


# Create a lambda function to square a number. Take input from user.
square = lambda x : x*x

n = int(input("Enter a number "))
print(square(n))


# In[ ]:




