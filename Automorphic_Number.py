n = int(input())
a = n*n
b = str(n)
c = str(a)
for i in range(len(c)):
    if b in c:
        print("Automorphic Number")
        break
    else:
        print("Not an Automorphic Number")
        break