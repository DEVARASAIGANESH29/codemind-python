p,r,t = map(int,input().split())
cp = p * (pow((1 + r / 100), t))
print(format(cp,".2f"))