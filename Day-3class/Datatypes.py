#numeric type
a=12
print(type(a))  
b=1.6
print(type(b))  
c=8+9j
print(type(c)) 
#string type
str="Python basics"
print(type(str))
print(len(str))
print(str[5])  
#list
d=[1,2,4,3,1]
print(type(d))  
d.append(20)
print(d)
d[4]=5
print(d)
#tuple
e=(1,2,6,3,4,1)
print(type(e))
print(e[5])
#dictionary
f={'name':'sai', 'age':'20'}
print(type(f))
print(f)
#set
g={1,2,1,4,5}
print(type(g))
print(g)
g.add(7)
print(g)
g.remove(2)
print(g)
#frozenset
h=frozenset({1,2,6,7,3,2})
print(type(h))
print(h)





