s=input()
u=0
l=0
for i in s:
  if i.isupper():
    u+=1
  elif i.islower():
    l+=1
    
print(u,l,end="")