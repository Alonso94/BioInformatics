list=[1, 2, 3, 4 , 1, 2]
def print_list(a):
    print('-'*10)
    for i in range(len(a)-1,-1,-1):
        print(i, a[i])
    print('-'*10)

print(list[3])
array=[[1.23432,2.232323,3,4],[3,2,1,3]]
n=len(array)
m=len(array[0])
print_list(array[0])
for i in range(n):
    for j in range(m):
        print("Element a[%d][%d]= %2.2f" %(i,j,array[i][j]))
en=enumerate(list)
for i,j in en:
    print(i,j)
print_list(list)
dict1={12:'Alonso', 13:'Paul', 14: 'CCC'}
print(dict1[12])
for i in dict1.keys():
    print(i,dict1[i])
print_list(list)