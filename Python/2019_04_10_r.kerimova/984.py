n=int(input())
m=input().split(' ')
m.sort(key=int)
# if n/2==int:
#     h=int((n//2)-1)
# else:
#     h=int((n//2)+1)
# print(h)
h = (n - 1) // 2
print(m[h])