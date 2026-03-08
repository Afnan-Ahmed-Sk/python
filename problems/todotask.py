list=[]
n=int(input("enter the number of list element:"))
for i in range (1,n+1):
    print(f"enter the {i} task to be added")
    e=input()
    list.append(e)
print(list)