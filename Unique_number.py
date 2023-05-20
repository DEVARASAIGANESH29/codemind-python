n = int(input())
a = str(n)
c=0
for i in a:
    if a.count(i)==1:
        c +=1
if len(a)==c:
    print("Unique Number")
else:
    print("Not Unique Number")
