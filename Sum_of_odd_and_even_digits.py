a = int(input())
k = list(map(int,input().split()))
v,b=0,0
for i in range(0,a,2):
    b+=k[i]
for i in range(1,a,2):
    v+=k[i]
if b-v==0:
    print("YES")
else:
    print("NO")