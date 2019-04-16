n=int(input())
numbers=input()
numlist=numbers.split()
for i in range(0,n):
    numlist[i]=int(numlist[i])
numlist.sort()
if n%2 == 0:
    print(numlist[int(n/2-1)])
else:
    print(numlist[int((n-1)/2)])