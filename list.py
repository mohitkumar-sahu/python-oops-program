l1=[10,20,30,40,50,10,10]
l2=[100,200,300,400,500]
# 1. Append
l1.append(60)
print(l1)

# 2. Clear all values in list
l2.clear()
print(l2)

# 3. sallow copy
l3=l1.copy()
print(l3)

# 4. To count a specfic value in list
x=l1.count(10)
print(x)

# 5. concatinate 2 list
l1.extend(l2)
print(l1)

# 6. To check index of an element
x=l1.index(30)
print(x)

# 7. insert a value at specific index
l2.insert(3,400)
print(l2)

# 8. Remove an element from given position
l2.pop()
print(l2)

# 9. remove only first occurence of given value from list
l1.remove(10)
l1.remove(10)
print(l1)

# 10. Reverse entire list
l1.reverse()
print(l1)

# 11. Sort the entire list in increasing and decreasing order
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)

# operation on list
l1=[10,20,30,40,50,10,10]
l2=[100,200,300,400,500]
l3=l1+l2
print(l3)
print(l1*2)