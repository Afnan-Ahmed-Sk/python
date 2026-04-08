# stop the input when it is q
lis=[]
while True:
    n=input("enter the element in list:")
    if n=='q':
        break
    else:
        lis.append(int(n))    
print(lis)