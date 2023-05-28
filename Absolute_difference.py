def is_prime(k):
    p=1
    np=1
    for i in k:
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
        if c>2:
            np*=i
        else:
           p*=i
    print(np-p)
n=int(input())
k=map(int,input().split())
is_prime(k)