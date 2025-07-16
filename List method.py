#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add(x, y=2):
    return x + y

print(add(3))


# In[1]:


a=[1,2,3,4]
a.append(5)
print(a)


# In[3]:


a=[1,2,3]
a.extend([4,5,6])
print(a)


# In[7]:


a=[1,2,3,4]
a.insert(2,34)
a.insert(1,'palak')
print(a)


# In[8]:


a=[1,2,3,4,5,6,7,8,9,0]
a.pop()
a.remove(1)
a.pop(2)
print(a)


# In[11]:


a=[1,2,3,4]
a.clear()
print(a)


# In[12]:


a=[1,2]
a.index(1)


# In[14]:


a=[21,32,342,123,2112,13]
a.sort()
print(a)
a.sort(reverse='true')
print(a)


# In[16]:


a=[]
n1=int(input("Enter number: "))
n2=int(input("Enter number: "))
n3=int(input("Enter number: "))
n4=int(input("Enter number: "))
n5=int(input("Enter number: "))
a.extend([n1,n2,n3,n4,n5])
print(a)


# In[18]:


a=[1,2,3]
b=[4,5,6]
a.extend(b)
print(a)


# In[19]:


a=[10, 20, 30, 40]
a.insert(2,25)
print(a)


# In[20]:


a=[10, 20, 30, 40]
a.remove(20)
print(a)


# In[22]:


a=[1, 2, 3, 4, 5]
print(a.pop())
print(a)



# In[23]:


a=[5, 10, 15, 20, 25]
a.index(15)


# In[24]:


a=[1, 2, 2, 3, 2, 4, 2]
a.count(2)


# In[26]:


a=[10, 5, 7, 3]
a.sort()
print(a)
a.sort(reverse='true')
print(a)


# In[27]:


a=[1, 2, 3, 4, 5] 
a.reverse()
print(a)


# In[32]:


a=[1,2,3]
b=a.copy()
print(a)
b.pop()
print(a)
print(b)


# In[5]:


a=[1,2,3,4,5,6,7,8,9]
for i in range(1,9):
    if a[i]%2==0:
        a.remove(i)
print(a)
    


# In[6]:


a=['Palak','Priya','Ram']
name=input("enter name: ")
a.remove(name)
print(a)


# In[13]:


a=[1,2,3,4,5,6,7,8]
num=int(input("Enter a number"))
print(a.index(num))
a.remove(num)
print(a)


# In[15]:


a=['palak','priya','anshika','komal']
a.sort()
print(a)


# In[21]:


[10*i*j for i in [1,2,3] for j in [4,5,6]]


# In[22]:


a=['java','python','python','c','c++']
a.count('python')


# In[23]:


a=[1,2,3]
b=a.copy()
print(a)
b.pop()
print(a)
print(b)


# In[34]:


a=[1,2,3,4,5,6,7]
b=len(a)/2
c=int(b)
a.insert(c,43)
print(a)


# In[41]:


a=tuple(["hello","cutie","mine","i","i"])
a.count("i")


# In[42]:


set_1={1,2,3}
set_2=set([1,2,3,4])
set_1.union(set_2)


# In[43]:


set_1={1,2,3}
set_2=set([1,2,3,4])
set_1.intersection(set_2)


# In[48]:


set_1={1,2,3}
set_2=set([1,2,3,4])
set_1.difference(set_2)


# In[49]:


set_1={1,2,3}
set_2=set([1,2,3,4])
set_1.issubset(set_2)


# In[52]:


set_1={1,2,3}
set_2=set([1,2,3,4])
set_1.isdisjoint(set_2)


# In[54]:


d={1:'one',2:'two'}
print(d)


# In[ ]:




