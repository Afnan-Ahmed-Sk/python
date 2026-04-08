tn=["tirunelveli","salem","erode","karur"]
kl=["thiruvantapuram","kollam","paalakaadu"]
an=["bangalore","mysore"]

tn2=tn                # tn and tn2 store same address of list element change in one affect another
print(tn2)

tn[3]="chennai"
print(tn)
print(tn2)

print("----------------")

tn3=tn.copy()       # in memory tn is separately created and tn3 pointing it so change in one does not affect another unless it is single list
tn.append("egmore")   # it is shallow copy
print(tn)                # tn3=tn[:] also same method
print(tn3)

In=[tn,kl,an]       # In 2 d list shallow copy that only copy outer list not copy inner list 
In2=In.copy()       # in that inner list that pionting reference of that list so change in inner list element affect the copy list
print("In2")
print(In2)
print("----------------")
In[0][0]="karaikudi"
print("In")
print(In)
print("In2")
print(In2)

# deep copy

import copy
In3=copy.deepcopy(In)
In[0][0]="kanchipuram"
print(In)
print(In3)

