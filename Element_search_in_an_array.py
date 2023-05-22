a = int(input())
n = map(int,input().split())
k = int(input())
for i in n:
    if k in n:
        print("True")
        break
    else:
        print("False")
        break