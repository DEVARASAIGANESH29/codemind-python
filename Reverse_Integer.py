n = input()
x = n[::-1]
a=[]
for i in x:
    a.append(i)
for j in range(0,len(a)):
    if a[0]=='0':
        a.remove(a[0])
    elif a[-1]=='-':
        a.remove(a[-1])
        a.insert(0,'-')
for l in a:
    print(l,end="")