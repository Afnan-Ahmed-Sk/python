list=[]
n=int(input("enter the no of element:"))
for i in range (n):
    a=int(input())
    list.append(a)

for i in range(n):
    if i==0:
        if list[i]>=list[i+1]:
            print(f"peak {list[i]}")
    elif i==n-1:
        if list[n-1]>=list[n-2]:
            print(f"peak {list[i]}")        
    else:
        if list[i]>=list[i-1] and list[i]>=list[i+1]:
            print(f"peak {list[i]}")
