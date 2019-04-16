q=int(input())
strarr=[]
for i in range(0,q):
    tempstr=input()
    strarr.append(tempstr)
strdict={}
for i in strarr:
    if strdict.get(i) is None:
        strdict[i]='OK'
    else:
        j=1
        tempi=i
        while strdict.get(i) is not None:
            i=tempi+str(j)
            j+=1
        strdict[i]=i
ans=list(strdict.values())
for i in ans:
    print(i)
         
