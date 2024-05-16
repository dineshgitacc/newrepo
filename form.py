# def func():
#     pass

a='World,love,I'
print(a[-1])
s=''
lst=[]
for i in a:
    if i == ",":
        lst.append(s)
        s=''

    else:
        s+=i
        
lst.append(s)
    
print(lst)


# a=5
# b=3

# a=[x for x in range(0,101)]
# print(a)

# c=[1,2,3,4,6,7,8,9,10]

# print(len(c))

# for i in range(1,len(c)):
#     if i not  in c:
#         print(i)
        

a="dinesh anand" 
b=[]
c=""

# print(a)

for i in  a:
    if i !=" ":
        c=c+i
        
        
    else:
         b.append(c)
         c="" 
b.append(c)           
print(b[::-1])

d=""

for i in b[::-1]:
    print(i)
    for j in i:
        # print(j)
        d=d+j
        # print(d)
    d=d+" "
print(d)   


# test_list = [1, 4, 5, 7, 8]

# list_len = sum(1 for i in test_list)

# print(list_len)
# a=(1 for i in test_list)
# for i in a:
#     print(i)

a=[3,2,8,5,1]
# b=(sorted(a))

# print(b)
n=len(a)

for j in range(n-1):
    for i in range(0,n-1):
        print(a[i])
        if a[i] > a[i+1]:  
            a[i],a[i+1]=a[i+1],a[i]
print(a)        

min_val=0  
max_val=0 
j=n-1 

for i in range(0,n-1):
    min_val+=a[i]
    
    max_val+=a[j]
    
    j-=1
print(min_val)    
print(max_val)   


b=[4,2,5,0,1,7,0]

for j in range(n-1):
    for i in range(0,n-1):
        print(a[i])
        if b[i] > b[i+1]:  
            b[i],b[i+1]=b[i+1],b[i] 
print(b)    


s="Hello how are you dinesh anand kavi"  
k=5     
a=""
lst=[]
count=0
for i in  s:
    if count==k:
        break
    if i==" ":
        count+=1
        lst.append(a)
        a=""
    else:
        a+=i
print(lst) 

a="$".join(['Hello', 'how', 'are', 'you', 'dinesh'])
print(a)
print(len(a))
print(list(a))
print(len(list(a)))
# v=""

# for i in lst:
#     v+=i 
#     v+=" "
# print(v.split(" "))       

a="hello "
print(len(a))
    
a=" "+"h"
print(a.split())
print(len(a ) )  


a="{[(})]"


openlist=["{","[","("]

closelist=["}","]",")"]

lst=[]

for i in a:
    if i in openlist:
        lst.append(i)
        print(lst)
    elif i in closelist:
        p=closelist.index(i)  
        
        if len(lst)>0 and (openlist[p]==lst[len(lst)-1] ):
            lst.pop()    
        
if len(lst)==0:
    print("balanced")    
else:
    print("unbalanced")       
        
    
    
import copy
li1 = [1, 2, [3,5], 4]
li2 = copy.copy(li1)
print ("The original elements before shallow copying")
for i in range(0,len(li1)):
    print (li1[i],end=" ")
print(id(li1))
 
print("\r")
li2[2][0] = 7
print ("The original elements after shallow copying")
for i in range(0,len( li1)):
    print (li1[i],end=" ")    
print(id(li1))  
    
    
# def outer(func)  :
#     def inner(a,b):
        
#         print("adding two numbers")  
        
#         print(func(a,b))
        
#         print("finisdhed")
        
#     return inner    
    
# @outer
# def add(a,b):
#     return a+b
# add(5,10)



# def decor1(func):
#     x=func()
#     return x*x
    

# def decor(func):
#     x=func()
#     return 2*x
        
# @decor1
# @decor
# def num():
#     return 10
# num()


class one:
    
    def __init__(self,string) -> None:
        
        print(string)
        
        
a=one("hello") 

# from multipledispatch  import dispatch

def fun(x,y):
    print(x+y)
    
def fun(x,y,z=0)    :
    print(x*y)
    
fun(3,4)    


class main:
    v=20
    
    def c(self):
        print(self.v)

    @staticmethod
    def a():
        print("hai")
        
    @classmethod
    def b(cls):
        print(cls.v)    
        
obj=main()
main.b()     
obj.c()  


# for i in range(5):
#     print("*" *i,end=" ")
#     print()

n=5
k = n - 1
for i in range(0, n):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i+1):
        print("* ", end="")
    print("\r")
 
n=5   
for i in range(5,0,-1):
        for j in range(0,i):
            print("* ",end="")
        print("\r") 
           
        
        
        
    
      
  
    
    
    
    
               
        
        
        
    

