n=input()
m=input()
k=n.split(" ")
q=m.split(" ")
l=[]
for i in range(0,len(k)):
    for j in range(0,len(q)):
        t=(int(k[i]),int(q[j]))
        l.append(t)
for i in l:
    print(i,end=" ")
