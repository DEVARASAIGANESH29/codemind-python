n = input()
let = n.split()
for i in range(0,len(let)):
    l =let[i]
    s = "".join(reversed(l))
    print(s,end=" ")