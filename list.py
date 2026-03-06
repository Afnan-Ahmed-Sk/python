number=[10,20,30,40,50]
# Accessing the list
print(number[:3])

print(number[:-3])

print(number[::-2])

# modifiying the list replace the element 
number[0]=5
print(number)

# insert at specific position
number.insert(0,3)

# add one element at last
number.append(90)
print(number)
# add list as nested list
number.append([60,70])
print(number)

number.extend([60,80])
print(number)

number2=number.copy()
print(number2)

print(number.count(50))

# delete the element not return the value
del number[0]
print(number)

# delete the specific element and return the deleted value
d=number.pop(4)
print(d)

e=number.pop()
print(e)

# remove by element
number.remove([60,70])
print(number)

#temporary sort
print(sorted(number))

print(number)

# permanent sort
number.sort()
print(number)

#reverse the list
number.reverse()
print(number)

# length if list
print(len(number))