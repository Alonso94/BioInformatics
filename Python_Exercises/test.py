p= [[1,2,3,5], [4,5,3,2],[3,6,5,4],[1,4,7,9]]
n= len(p)
b= len (p[0])
for i in range (n):
    for j in range (b):
        print ("P[%d,%d]= %d"%(i, j, p[i][j]))

def print_dict(id, dictionary):
    for i in dictionary.keys():
        print ("%d %s : %s" %(id, i, dictionary[i]))

history= {'2017-2018': 'preparatory', '2018-2020': 'master', '2020- till now': 'phd'}
print_dict(id=3, dictionary=history)
family={'father': 'Xxxxx', 'Mother':'Xxxxx', 'Brother':'Xxxxx'}
print_dict (id=2, dictionary=family)






