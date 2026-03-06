name="afnan ahmed"
print(name.upper())
print(name.lower())
print(name.title())
print("armam \t ahmed")
print("arman \n ahmed")
print(len(name))
print(name.isalpha())
print(name.isdigit())
print(name.count("a"))
print("ahmed" in name) # in is a keyword that check particular character in a string
print("arman" not in name)  # not in is a keyword that check particular character in a string

# multiple assignment
name1, age, location="afnan", 23, "madurai"  
print(age) 

x=y=z=100
print(y)

otp=12345
print("this is one time otp",otp)
print("this is one time opt"  + str(otp))
print(type(otp))