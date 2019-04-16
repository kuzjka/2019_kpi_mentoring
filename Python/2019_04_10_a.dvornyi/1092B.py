n=int(input())
skilllist=input()
skilllist=skilllist.split()
for i in range(0,n):
    skilllist[i]=int(skilllist[i])
skilllist.sort()
result=0
for i in range(0,n):
    if i%2 != 0:
        pass
    else:
        result=result+(skilllist[i+1]-skilllist[i])
print(result)