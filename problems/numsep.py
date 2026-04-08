str_id="32,45,56,23,67"
temp=" "
lis=[]
for i in str_id:
    if i==",":
        lis.append(int(temp))
        temp=" "
        continue

    else:
        temp=temp+i      
lis.append(int(temp))
print(lis)
print(type(lis))