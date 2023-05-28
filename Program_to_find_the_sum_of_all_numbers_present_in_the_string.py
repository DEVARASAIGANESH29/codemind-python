a = input()
c = 0
for i in a:
    if i.isdigit() is True:
        c+=int(i)
print(c)