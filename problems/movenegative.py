lis=[]
n=int(input("enter the no of element :"))
for i in range(n):
    a=int(input())
    lis.append(a)
print(f"list of element {lis}")  
i=0  
while i< n:
    if lis[i]<0 :
        p=lis.pop(i)
        lis.append(p)
        n-=1
    else:
        i+=1    
print(f"list of element {lis}")        