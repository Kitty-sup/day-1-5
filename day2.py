#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=46.8
print(int (a))



# In[2]:


x = 0
if x:
    print('True')
else:
    print('False')



# In[25]:


a=int(input("Enter a number: "))
print(a)
if a>0:
    print('Positive')
elif a==0:
    print('zero')
else:
    print('Negative')


# In[26]:


a=int(input("Enter your age: "))
if a<18:
    print('teen')
elif a<13:
    print('child')
else:
    print('Adulr')


# In[32]:


a=int(input("Enter a number: "))
if a%2==0:
    print('even')
if a==10:
    print("number is 10")
else:
    print('odd')


# In[33]:


a=int(input("Enter a number: "))
if a>90:
    print('A')
elif a>75:
    print('B')
elif a>45:
    print("C")
else:
    print("fail")


# In[11]:


n=str(input("Enter a string: "))
if len(n)>5:
    print('lenghty')
else:
    print('short')


# In[22]:


month=str(input("enter no"))
winters=['jan','feb','dec','march']
summers=['april','may','june','july']
monsoon=['august','sep','oct','nov']
if month==winters:
    print("winter")
elif month==summers:
    print("summers")
else:
    print("monsoon")


# In[24]:


age =int(input("enter"))
if age<15:
    print("still okey")
else :
    print("expire")


# In[47]:


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
if a>b and a>c:
        print("A is greatest")
elif b>a and b>c:
        print("b is greatest")
else:
        print("c is greatest")


# In[ ]:


a=0
while(a<3):
    a=a+1
    print("heloooooooooooo")


# In[8]:


a=5
b=3
print(a&b ,a^b ,a<<1,a<<1,~a)


# In[13]:


name="Palak"
name=7.45243
print(name)
print(int(name))


# In[18]:


x, y =10,20
if x>y:
        if x==y:
            print("x is equal to y")
        else:
            print("x is not equal to y")
else:
    print("x is smaller then y")


# In[16]:


x = 15
if x > 10:
    if x < 20:
        print("x is between 10 and 20")
    else:
        print("x is 20 or more")
else:
    print("x is 10 or less")


# In[ ]:




