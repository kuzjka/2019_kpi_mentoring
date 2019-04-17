q=int(input())
names = set()
for i in range(0,q):
    name = input()
    if name in names:
        original = name
        suffix = 1
        name = original + str(suffix)
        while name in names:
            suffix += 1
            name = original + str(suffix)
        print(name)
    else:
        print("OK")
    names.add(name)