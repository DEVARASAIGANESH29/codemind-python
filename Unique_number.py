a = input()
c=0
for i in a:
    if a.count(i)==1:
        c+=1
if c==len(a):
    print("Unique Number")
else:
    print("Not Unique Number")