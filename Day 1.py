#!/usr/bin/env python
# coding: utf-8

# In[13]:


a = int(input("Enter a number"))
b = int(input("Enter second number"))

print("Enter 1 Addition")
print("Enter 2 Subtraction")
print("Enter 3 Multiplication")
print("Enter 4 Division")
ch = int(input("Enter choice"))
if(ch == 1):
    print("Addition : " , a+b)

elif(ch == 2) : 
    print("Subtractio : " , a-b)
elif(ch == 3) :
    print("Multiplication : " , a*b)

elif (ch == 4):
    print("Division : " , a/b)


# In[14]:


a = 5
a += 5
print(a)

a -= 5
print(a)

a *= 5
print(a)

a /= 5
print(a)


# In[7]:


a =+ 5
print(a)

a = -5
print(a)




# In[16]:


a = 5
b = 2;

print(a == b)
print(a <= b)
print(a <= b)
print(a != b)


# In[18]:


print(2 == 2 and 3 == 2)
print(2>3 or 2<3)
print(not(2>3))


# In[4]:


print(5 & 4)
print(5 | 4)
print(~5)


# In[5]:


a = 5
b = 6
print(a is b)
print(a is not b)


# In[8]:


l1 = [1,2,3,4,5]
print(12 in l1)
print(12 not in l1)


# In[ ]:




