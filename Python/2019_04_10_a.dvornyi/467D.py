n=input()
words=input()
arrwords=words.lower().split()
sn=int(input())
dict=[]
for i in range(0,sn):
    pair=input()
    dictpair=pair.lower().split()
    dict.append(dictpair)
for i in range(0,len(dict)):
    for j in dict:
        if dict[i][1]==j[0]:
            dict[i]=[dict[i][0],j[1]]
dicts=sorted(dict,key=lambda a: len(a[1]),reverse=True)
dict=sorted(dicts,key=lambda a: a[1].count('r'),reverse=True)
for i in range(0,len(arrwords)):
    for j in dict:
        if arrwords[i]!=j[0]:
            pass
        else:
            if arrwords[i].count('r') > j[1].count('r'):
                arrwords[i]=j[1]
            elif arrwords[i].count('r')==j[1].count('r') and len(arrwords[i]) > len(j[1]):
                arrwords[i]=j[1]
            else:
                pass
finstr=''.join(arrwords)
print(finstr.count('r'),len(finstr))
