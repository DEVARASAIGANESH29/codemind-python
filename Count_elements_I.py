a,b=map(int,input().split())
k = list(map(int,input().split()))
h = list(map(int,input().split()))
c=0
o=0
p=[]
for i in k:
    for j in h:
        if i in h and j in k:
            p.append(i)
            p.append(j)
l = set(p)
for u in l:
    c+=1
print(c)
            
            
            

        