# using iterable
var=(1,2,3,4,5)
for v in var:
    print(v,end=" ")
print()
# using Range
for i in range(5):
    print(var[i],end=" ")
print()
i=0
# using While Loop
while i<len(var):
    print(var[i],end=' ')
    i+=1
print()
t=(1,2,3,4,5,6,7,6,5,4,3,2)
print(t.count(2))

print(t.index(5))

t1=(1,2,3,4,5,6,7,6,5,4,3,2)
t2=(10,20,30,40,50)
T=t1+t2
print(T)
T=t1*3
print(T)