p=3
list=[2]
c=2
k=0

while c < 1000 :
    for i in list :
        t=p**0.5
        if(i > t):
            break 
        if(p%i==0):
            p=p+1
            k=1
            break
        
    if(k==0):
        list.append(p)
        p+=1
        c+=1
    k=0
print(list)
