list=[2,3]
c=2
p=5
k=0

while c<1000 :
    t=p**0.5
    for i in list:
        if (i>t) :
            break
        if (p%i==0) :
            k=1
            p=p+1
            break
    if (k==0) :
       list.append(p)
       p=p+1
       c=c+1
    k=0
print(list)

