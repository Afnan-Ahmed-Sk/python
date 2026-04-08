user={
    "name":"afnan",
    "age":20,
    "place":"chennai",
    "mobile":23432545,
    "dept":"cse"
}

# accessing dictionary

print(user["place"])
print(user["dept"])
print(user["mobile"])

# modifying dictionary

user["place"]="maduari"
user["age"]=43
print(user)


# deleting key

del user["mobile"]
print(user)

# looping

for k ,v in user.items():
    print(f"key : {k}")
    print(f"value : {v}")

for k in user.keys():
    print(f"key : {k}")    

for v in user.values():
    print(f"values : {v}")    

# list of dictionary

users=[]
user1={
    "name":"abilash",
    "age":34
}
user2={
    "name":"athif",
    "age":34
}
users.append(user1)
users.append(user2)
print(users)
print(users[0]["name"])
print(users[1]["age"])