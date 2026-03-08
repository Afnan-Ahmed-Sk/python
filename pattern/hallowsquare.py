r=int(input("enter the row :"))
c=int(input("enter the column :"))
for i in range (r):
    for j in range (c):
        if i==0 or i==r-1 or j==0 or j==c-1:
            print("*",end="")
        else:
            print(" ",end="")    
    print()        