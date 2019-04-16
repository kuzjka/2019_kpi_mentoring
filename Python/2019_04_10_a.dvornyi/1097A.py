cur=input()
hand=input()
arrhand=hand.split()
yes=0
for j in range(0,4):
    if arrhand[j][0]==cur[0] or arrhand[j][1]==cur[1]:
        yes=1
    else:
        pass
if yes==1:
    print("YES")
else:
    print("NO")