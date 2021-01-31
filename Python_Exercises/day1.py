x= float(input("the first number is "))
y= float(input("the second number is "))
res= []
res.append (x+y)
res.append (x*y)
res.append (x//y)
res.append (x/y)
res.append (x-y)
# print (res[2])
min=100000
index=0
for i,m in enumerate(res):
    print(i,m)
    if m<min:
        min=m
        index=i
print (index,min)
k= res[0]
res[0]=res [2]
res [2]= k
for i,m in enumerate(res):
    print(i,m)
