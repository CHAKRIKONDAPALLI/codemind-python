a=int(input())
b=int(input())
for i in range(a,b+1):
    c=0
    c1=0
    temp=i
    while(temp>0):
        r=temp%10
        c1=c1+1
        if(r>0):
            if(i%r==0):
                c=c+1
        temp=temp//10
    if(c==c1):
            print(i,end=' ')