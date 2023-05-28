a = int(input())
b = a*a
k = 0
for i in range(b):
    d = b%10
    k  += d
    b = b//10
if k==a:
    print("Neon Number")
else:
    print("Not Neon Number")