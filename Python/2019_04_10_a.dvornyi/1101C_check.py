import itertools
import copy

def solve(data):
    workarr = data
    workarr.sort()
    workarr[0].append(1)
    x = 0
    for j in range(1, len(workarr)):
        if workarr[j][0] <= workarr[j - 1][1]:
            workarr[j].append(x % 2 + 1)
        else:
            x += 1
            workarr[j].append(x % 2 + 1)
    y = 0
    for j in range(0, len(workarr)):
        if workarr[j][3] == 1:
            y += 1
        else:
            pass
    if y == len(workarr):
        # print("-1")
      return -1
    else:
        for j in range(0, len(workarr)):
            workarr[j][0] = workarr[j][2]
        workarr.sort()
        result = []
        for j in range(0, len(workarr)):
            result.append(workarr[j][3])
            # print(workarr[j][3], end=" ")
        # print("")
        return result

lengths = itertools.product(range(1, 7), repeat=2)
lengths = map(lambda t: list(t), lengths)
lengths = list(filter(lambda d: d[0] <= d[1], lengths))
print(lengths)

for data in itertools.product(lengths, repeat=3):
    data = list(data)
    # for d in enumerate(data):
    #     d[1].append(d[0])
    input = []
    for d in enumerate(data):
        input.append([d[1][0], d[1][1], d[0]])
    data = copy.deepcopy(input)
    print("data:", data)
    result = solve(data)
    if result != -1:
        for i in range(1, 7):
            present1 = 0
            present2 = 0
            for j in range (0, 3):
                if (i >= input[j][0] and i <= input[j][1]):
                    if (result[j] == 1): present1 += 1
                    else: present2 += 1
            if (present1 > 0 and present2 > 0):
                print("input:", input, "data: ", data, "result: ", result, "intersects in: ", i)
                raise StopIteration