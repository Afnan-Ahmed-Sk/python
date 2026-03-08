import random
num=random.randint(1,20)
print(num)
gess=int(input("enter the no :"))
while num!=gess:
    print("number is not equal")
    gess=int(input("enter the the no :"))
print("number is equal")