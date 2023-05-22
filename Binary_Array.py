n = int(input())
k = list(map(int,input().split()))
v = 0
for i in k:
    if i==0 or i==1:
        v+=1
if v==n:
    print("True")
else:
    print("False")