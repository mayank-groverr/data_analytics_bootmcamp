#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Whille loop
num = int(input("Enter a number : "))
i = 1

while i<=10 :
    print(f"{num} x {i} = {num * i}")
    i += 1


# In[3]:


char = (input("Enter Character"))
print("Entere
while(char != 'Q'):
    char = (input("Enter Character"))
    


# In[4]:


i = 3
password = 1234
num = int(input("Enter password"))
if(num != password):
    while(password != num):
        if(i == 0):
            print("Try after some time")
            break
        else:
            if num == password:
                    break;  
            else:
                i -= 1
                print("Attempts Left", i)
                num = int(input("Enter password"))
              
else:
    print("Access GRanted")
       


# In[ ]:





# In[1]:


i = 7
while i <= 100:
    if i % 7 == 0:
        print(i)
    i += 1 


# In[6]:


for i in range(1,6):
    print("Number : " , i)


# In[9]:


for i in range(1,11):
    print(f"{2} x {i} = {2*i}")


# In[10]:


attempt = 3
password = 1234
for i in range(1,4):
    num = int(input("Enter password"))
    if num != password:
        attempt -= 1
        print("Attempt left" , attempt)
        if i == 3:
            print("Limit reached")
            
        
    else:
        print("Acess Granted")
        break
    


# In[12]:


for  i range(1, 10):
    if i == 5:
        continue
    if i == 8:
        break
    print(i)


# In[1]:


attempt = 4
orn = 1234
passwor = input("Enter password").lower();
for i in range(1, 6):
    passwor = input("Enter password").lower();
    if passwor == "forgot":
        attempt -= 2
        print("Attempt", attempt)
        continue
    if passwor == orn :
        print("Access Granted")
        break
    if attempt == 1:
        attempt -= 1;
        print("Attempt" , attempt)
        break
attempt -= 1;            
print("Attempt" , attempt)
   


# In[28]:


for i in "Python Programming":
    if i == 'n':
        break;
    if i == 'o':
        continue
    print(i)




