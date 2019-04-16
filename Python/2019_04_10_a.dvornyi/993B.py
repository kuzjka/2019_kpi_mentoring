q=input()
q1=input()
q2=input()
q1arr=q1.split()
q2arr=q2.split()
parr1=[]
for i in range(0,len(q1arr),2):
    pair=[q1arr[i],q1arr[i+1]]
    parr1.append(pair)
parr2=[]
for i in range(0,len(q2arr),2):
    pair=[q2arr[i],q2arr[i+1]]
    parr2.append(pair)
matches={}
for i in parr1:
    curmatch={}
    for j in parr2:
        if i[0]==j[0] and i[1]==j[1]:
            continue
        elif i[0]==j[0] or i[0]==j[1]:
            curmatch[i[0]]=1
        elif i[1]==j[1] or i[1]==j[0]:
            curmatch[i[1]]=1
        else:
            pass
    if len(curmatch)==2:
        print("-1")
        break
    else:
        matches.update(curmatch)
    if len(matches)==2:
        print("0")
        break
    else:
        pass
if len(matches)==1:
    ans=list(matches.keys())
    print(ans[0])
else:
    pass