a = int(input())
b =str(a)
k = 0
x =1
for i in b:
    d = a%10
    k += d
    x *= d
    a = a//10
if(k == x):
    print("Spy Number")
else:
    print("Not Spy Number")