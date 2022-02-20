#!/usr/bin/env python
# coding: utf-8

# In[169]:


#LIST
#1
list = ['python','php','java']
for i in list:
    print(i)
#2 
list2 = [2, 5, 8, 9, 77, 53, 12, 24, 11, 69, 75]
a=0
for i in list2:
    a = a+i
print(a)
#3
list3 = []
n = int(input('Хэдэн өгөгдөл бичих вэ?-'))
for i in range(0,n):
    b=int(input())
    list3.append(b)
print(list3)
c=1
for i in list3:
    c=c*i
print(n,'өгөгдөл бүхий жагсаалтын үржвэр =',c)
#4
list4 = []
n = int(input('Хэдэн өгөгдөл бичих вэ?-'))
for i in range(0,n):
    b=int(input())
    list4.append(b)
print(list4)
print("3дахь болон сүүлийн элементийн үржвэр",int(list4[2]*list4[-1]))
#5
list5 = []
n = int(input('Хэдэн өгөгдөл бичих вэ?-'))
for i in range(0,n):
    b=int(input())
    list5.append(b)
print(list5)
print(max(list5))
print(min(list5))
#6
#7
list7 = []
n = int(input('Хэдэн өгөгдөл бичих вэ?-'))
for i in range(0,n):
    b=input()
    list7.append(b)
print(list7)
a=set(list7)
print('Давхардаагүй утгууд',a)
#8
list8 = []
n = int(input('Хэдэн өгөгдөл бичих вэ?-'))
for i in range(0,n):
    b=int(input())
    list8.append(b)
print(list8)
k=0
for i in list8:
    k=k+1
if k>0:
    print("list8 хоосон биш")
else:
    print("list8 хоосон")
#9
list9 = [0,1,2,3,4,5,6,7,8,9]
del list9[3]
del list9[4]
del list9[5]
print('LIST9',list9)
#Tuple
#10
x = (1, 2, 3, 5 , 8 , 9)
print('TUPLE1',x)
#11
b=[]
for i in x:
    b.append(i)
n=int(input())
b.append(n)
print(b)
#12
b=[]
for i in x:
    b.append(i)
print(b)
print(b[1],b[-2])
#13
print(x)
n=int(input())
print(n in x)
#14
print(x)
for i in x:
    print(i)
#Set
#15
Set1= {'ab','cd','fdf',1,2,5,23}
Set2= {'ab',1,3,4,11,'fdf'}
Set3= Set1.union(Set2)
print(Set3)
#16
Set4=Set1.intersection(Set2)
print(Set4)
#17
A1=[]
print('хэдэн өгөгдөл бичих вэ?')
n=int(input())
for i in range(0,n):
    A1.append(int(input()))
Set5=set(A1)
print('Шинэ Сэт =',Set5)
print('Шинэ үүсгэсэн сэтний урт',len(Set5))
print('сэт2 урт', len(Set2))
#18
print(Set5)
l=int(input())
Set5.discard(l)
print(Set5)
#19
Set2.clear()
print(Set2)
#20
del Set2
# Dict
#21
dict1 = { 
1: 95, 
3: 90, 
2: 91 } 
print(dict1)
x = dict1[1]
print(x)

#22
print(dict1)
n=int(input())
if n in dict1:
    print(n,"is in dict1")
else:
    print(n,"isnt in dict1")
#23
j=int(input())
m=[]
for i in dict1:
    m.append(dict1[i])
print(m)
if j in m:
    print('yes',j,'is in dict1')
else:
    print("No")
#24
for x,y in dict1.items():
    print(x,y)
#25
dict2 = { 
'Manufacturer': 5, 
'Model': 3, 
'Year': 2021 } 
z=dict1.update(dict2)
print(dict1)
#26
print("end")
    

    


# In[ ]:





# In[ ]:





# In[168]:


#LIST
#1
list = ['python','php','java']
for i in list:
    print(i)
#2 
list2 = [2, 5, 8, 9, 77, 53, 12, 24, 11, 69, 75]
a=0
for i in list2:
    a = a+i
print(a)
#3
list3 = []
n = int(input('Хэдэн өгөгдөл бичих вэ?-'))
for i in range(0,n):
    b=int(input())
    list3.append(b)
print(list3)
c=1
for i in list3:
    c=c*i
print(n,'өгөгдөл бүхий жагсаалтын үржвэр =',c)
#4
list4 = []
n = int(input('Хэдэн өгөгдөл бичих вэ?-'))
for i in range(0,n):
    b=int(input())
    list4.append(b)
print(list4)
print("3дахь болон сүүлийн элементийн үржвэр",int(list4[2]*list4[-1]))
#5
list5 = []
n = int(input('Хэдэн өгөгдөл бичих вэ?-'))
for i in range(0,n):
    b=int(input())
    list5.append(b)
print(list5)
print(max(list5))
print(min(list5))
#6
#7
list7 = []
n = int(input('Хэдэн өгөгдөл бичих вэ?-'))
for i in range(0,n):
    b=input()
    list7.append(b)
print(list7)
a=set(list7)
print('Давхардаагүй утгууд',a)
#8
list8 = []
n = int(input('Хэдэн өгөгдөл бичих вэ?-'))
for i in range(0,n):
    b=int(input())
    list8.append(b)
print(list8)
k=0
for i in list8:
    k=k+1
if k>0:
    print("list8 хоосон биш")
else:
    print("list8 хоосон")
#9
list9 = [0,1,2,3,4,5,6,7,8,9]
del list9[3]
del list9[4]
del list9[5]
print('LIST9',list9)
#Tuple
#10
x = (1, 2, 3, 5 , 8 , 9)
print('TUPLE1',x)
#11
b=[]
for i in x:
    b.append(i)
n=int(input())
b.append(n)
print(b)
#12
b=[]
for i in x:
    b.append(i)
print(b)
print(b[1],b[-2])
#13
print(x)
n=int(input())
print(n in x)
#14
print(x)
for i in x:
    print(i)
#Set
#15
Set1= {'ab','cd','fdf',1,2,5,23}
Set2= {'ab',1,3,4,11,'fdf'}
Set3= Set1.union(Set2)
print(Set3)
#16
Set4=Set1.intersection(Set2)
print(Set4)
#17
A1=[]
print('хэдэн өгөгдөл бичих вэ?')
n=int(input())
for i in range(0,n):
    A1.append(int(input()))
Set5=set(A1)
print('Шинэ Сэт =',Set5)
print('Шинэ үүсгэсэн сэтний урт',len(Set5))
print('сэт2 урт', len(Set2))
#18
print(Set5)
l=int(input())
Set5.discard(l)
print(Set5)
#19
Set2.clear()
print(Set2)
#20
del Set2
# Dict
#21
dict1 = { 
1: 95, 
3: 90, 
2: 91 } 
print(dict1)
x = dict1[1]
print(x)

#22
print(dict1)
n=int(input())
if n in dict1:
    print(n,"is in dict1")
else:
    print(n,"isnt in dict1")
#23
j=int(input())
m=[]
for i in dict1:
    m.append(dict1[i])
print(m)
if j in m:
    print('yes',j,'is in dict1')
else:
    print("No")
#24
for x,y in dict1.items():
    print(x,y)
#25
dict2 = { 
'Manufacturer': 5, 
'Model': 3, 
'Year': 2021 } 
z=dict1.update(dict2)
print(dict1)
#26


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




