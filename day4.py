#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def hello():
    print("helloo")
hello()            
def sum(a,b):
    print(a+b)
sum(3,4)


# In[ ]:


def SI(p,r,t):
    print((p*r*t)/100)
SI(32,33,2)


# In[ ]:


def table(n):
    for i in range(0,11):
        print(n*i)
table(2)


# In[8]:


print("helooo")


# In[3]:


def sum_n(a,b):
    sum=0
    for i in range(a,b):
        sum+=i
        print(sum)
    print(sum)
sum_n(1,10)


# In[7]:


def sum_n(a,b):
    sum=0
    for i in range(a,b):
        if i%2!=0:
            sum+=i
            print(sum)
    print(sum)
sum_n(1,51)


# In[13]:


def sum(a,b):
    c=a+b
    return c
sum(3,4)


# In[22]:


add=lambda a,b,c: a+b+c
add(10,10,30)
subtract=lambda a,b: a-b
subtract(10,5)


# In[31]:


def hello():
    print("hello")
    def hii():
        print("hii")
    hii()
hello()


# In[36]:


def hello():
    print("hello")
    def sum(a,b):
        c=a+b
        return c
    sum(1,1)
hello()


# In[42]:


try:
    def rev(word):
        print(word[::-1])
    rev("palak")
except Exception:
    print("exception")
else:
    print("jo bhi h")
finally:
    print("done")


# In[44]:


def square(n):
    m=n**2
    return m
square(3)


# In[45]:


def sum(a,b):
        c=a+b
        return c
sum(1,1)


# In[48]:


def even(n):
    if n%2==0:
        return n
    else:
        print("number is odd")
even(4)


# In[79]:


def rev(word):
    a=word[::-1]
    if a==rev:
        print("String is peleandrome")
    else:
        print("string is not pelandrome")
rev("mom")



# In[53]:


def largest(a):
    z=max(a)
    return z
largest([1,2,3,44])


# In[55]:


def fact(x):
    fact=1
    for x in range(1,x+1):
        fact*= x
        print(fact)
fact(4)


# In[56]:


n = int(input("enter"))
n1, n2 = 0, 1
count = 0
if n <= 0:
   print("enter a no.")
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


# In[59]:


def fibo(n):
    n1, n2 = 0, 1
    count = 0
    if n <= 0:
       print("enter a no.")
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
fibo(6)


# In[ ]:





# In[75]:


def isPalindrome(n):
    num = str(n) 
    reversed_num = num[::-1]  

    if num == reversed_num:  
        return True
    return False
isPalindrome("wow")


# In[80]:


def rev(word):
    num =str(n)
    a=num[::-1]
    if a==num:
        print("String is peleandrome")
    else:
        print("string is not pelandrome")
rev("mom")


# In[ ]:





# In[82]:


type(lambda x: x)


# In[83]:


def foo(): pass
print(foo())


# In[ ]:





# In[87]:


sum(7,7)


# In[88]:


bool('False')


# In[89]:


def foo(a, b=1): return a+b


# In[91]:


def countvowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in word:
        if ch in vowels:
            count += 1
    return count
a = input("Enter a string: ")
print("Number of vowels:", countvowels(a))


# In[93]:





# In[96]:


def sum(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
sum(3,3,3)    


# In[ ]:





# In[3]:


def odd(n):
    if n%2==0:
        print("number is even")
    else:
        print("number is odd")
odd(5)


# In[5]:


def avg(a,b):
    c=(a+b)/2
    return c
avg(3,3)


# In[6]:


add=lambda a,b,c: a+b+c
add(10,10,30)
subtract=lambda a,b: a-b
subtract(10,5)


# In[7]:


square=lambda a:a**2
n=int(input("Enter the number: "))
square(n)


# In[9]:


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

num = int(input("Enter"))
print("", factorial(num))


# In[ ]:




