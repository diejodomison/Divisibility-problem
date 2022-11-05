x=int(input())
y=int(input())
k=0
for i in range(1000,2001):
    if i%x==0 and i%y==0:
        k=k+i
print(k)

