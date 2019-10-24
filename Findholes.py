s1=input("")
l0=['C','E','F','G','H','I','J','K','L','M','N','S','T','U','V','W','X','Y','Z']
l1=['A','D','O','P','Q','R']
l2=['B']
s=0
for i in s1:
  if i in l0:
    s+=0
  elif i in l1:
    s+=1
  else:
    s+=2

print(s,end="")