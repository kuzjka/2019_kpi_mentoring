q=int(input())
qarr=[]
for i in range(0,q):
    intnum=int(input())
    intnumarr=[]
    for j in range(0,intnum):
        size=input()
        size=size.split()
        for k in range(0,2):
            size[k]=int(size[k])
        size.append(j)
        intnumarr.append(size)
    qarr.append(intnumarr)
for i in range(0,q):
    workarr=qarr[i]
    workarr.sort()
    workarr[0].append(1)
    x=0
    for j in range(1,len(workarr)):
        if workarr[j][0] <= workarr[j-1][1]:
            workarr[j].append(x%2+1)
        else:
            x+=1
            workarr[j].append(x%2+1)
    y=0
    for j in range(0,len(workarr)):
        if workarr[j][3]==1:
            y+=1
        else:
            pass
    if y==len(workarr):
        print("-1")
    else:
        for j in range(0,len(workarr)):
            workarr[j][0]=workarr[j][2]
        workarr.sort()
        for j in range(0,len(workarr)):
            print(workarr[j][3],end=" ")
        print("")