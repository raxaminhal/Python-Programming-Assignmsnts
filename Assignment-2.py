#!/usr/bin/env python
# coding: utf-8

# In[4]:


sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
print(avg)
if(avg>=90):
    print("Grade: A")
elif(avg>=80 and avg<90):
    print("Grade: B")
elif(avg>=70 and avg<80):
    print("Grade: C")
elif(avg>=60 and avg<70):
    print("Grade: D")
else:
    print("Grade: F")


# In[6]:


num = int(input("Enter a number: "))
if (num % 2) == 0:
   print(" Input Number Is Even Number")
else:
   print(" Input Number Is Odd Number")


# In[8]:


n = len([10, 20, 30 ,40]) 
print("The length of list is: ", n) 


# In[10]:


list1 = [181, 55, 87, 8, 89] 
total = sum(list1)
print("Sum of all elements in given list: ", total) 


# In[11]:


list1 = [10, 20, 4, 45, 99] 
print("Largest element is:", max(list1)) 


# In[13]:


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:

    if i<5:

        print(i)


# In[ ]:




