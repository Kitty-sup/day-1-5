#!/usr/bin/env python
# coding: utf-8

# In[ ]:


while True:
    n=input("type q to exit: ")
    if n=='q':
        print("exited")
        break
    else:
        print("you typed : ",n)
    


# In[ ]:


while True:
    user_input=input("type 'q' to quit:")
    if user_input=='q':
        print("exited loop!")
        break
    else:
        print("you typed",user_input)


# In[ ]:


password = "open123"
i=3
while i>0:
    user_input=input("enter Password: ")
    if user_input==password:
        print("Access granted😊")
        break
    else:
        i-=1
        print(f"wrong password!! {i} Attemts left(●'◡'●)(●'◡'●).")


# In[ ]:


i=1
while i<100:
    if i%7==0:
        print(f"{i} is divisble")
    i+=1


# In[3]:


num = int(input("Enter number: "))
for i in range(1,11):
    print(f"{num}*{i}={num*i}")


# In[ ]:


password = "open123"
for i in range(0,3):
    user_input=input("enter Password: ")
    if user_input==password:
        print("Access granted😊")
        break
    else:
        print(f"wrong password!! {2-i} Attemts left(●'◡'●)(●'◡'●).")


# In[6]:


for i in range(1,11):
    if i==3:
        continue
    elif i==8:
        break
    print(i)


# In[ ]:


for i in range(0,5):
    n=input("type password : ")
    if n=='forget':
        i-=1
        continue
    elif n=='palak':
        print("you typed palak : ")
        break
    else:
        i-=1
        print(f"attemt left {4-i}")
    


# In[ ]:


str="python"
i=len(str)
for i in range(0,7):
    if i==5:
        continue
    elif i==6:
        break
    print(str)
    
    


# In[ ]:


word = "PYTHONPROGRAMMING"

for letter in word:
    if letter == 'O':
        continue   
    if letter == 'N':
        print("🛑 Breaking at 'n'")
        break     
    print("✅ Letter:",letter)


# In[ ]:





# In[ ]:


def sum(a,b):
    ans=a+b
    print(ans)

sum(4,4)
    


# In[1]:


def rev(word):
    print(word[::-1])
rev("palak")


# In[ ]:


print(10 / 5)


# In[ ]:


print(3**2)


# In[ ]:


type('5') 


# In[ ]:


type(5) 


# In[ ]:


x = 5
if x > 3: 
    print('Yes')
    if x>3:
        print('yess')


# In[ ]:


if (5 < 10):
    print('OK')


# In[ ]:


if x==0:
    print('Hello') 


# In[ ]:


print(4==4 & 5==5)


# In[ ]:


if x=5; elif x==6:


# In[ ]:


if 3 > 2 and 2 < 5:


# In[ ]:


for i in range(1,10,3): print(i)



# In[ ]:


while False: 
    print('Hi')


# In[ ]:


for x in [1,2,3]: print(x)


# In[ ]:


'python'[0]


# In[ ]:


len('hello')


# In[ ]:


print('Hello, World!')


# In[ ]:


n=int(input("Enter number: "))
m=int(input("Enter number: "))
if n>m:
    print("N is largest")
else:
    print("M is largest")



# In[ ]:


n=int(input("Enter number: "))
if n>0:
    print("number is positive")
else:
    print("number is negative")


# In[ ]:


num = int(input("Enter number: "))
i=1
while i<11:
    print(f"{num}*{i}={num*i}")
    i+=1


# In[2]:


i=1
while i<11:
    print(i)
    i+=1


# In[17]:


n=[1,2,3,4,5,6]
for i range(0,5):
    if n[i]%2==0
        print(f"{[n]}")


# In[12]:


n = int(input("enter"))
n1, n2 = 0, 1
count = 0
if n <= 0:
   print("Enter a no.")
elif n == 1:
   print("Fibonacci sequence upto",n)
   print(n1)
else:
   print("Fibonacci:")
   while count < n:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1


# In[15]:


def prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


print(prime(11)) 



# In[3]:


s = "Python"
print(s[0:3])    
print(s[::2])    
print(s[-1])


# In[ ]:




