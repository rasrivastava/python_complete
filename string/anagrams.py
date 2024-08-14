# input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]

# test = {}

# for word in input_list:
#     #import pdb; pdb.set_trace()
#     key = ''.join(sorted(word))
#     if key in test:
#         test[key].append(word)
#     else:
#         test[key] = [word]

# print(test)
# # {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}


# result = []
# for group in test.values():
#     result.append(group)
#     # import pdb; pdb.set_trace()
#     # if len(group) > 1:
#     #     result.append(group)
#     # else:
#     #     result.append(group[0])

# print(result)
# # [['eat', 'tea', 'ate'], ['tan', 'nat'], 'bat']

s1 = {"eat", "nat", "bat", "tab", "tea", "ate", "art"}

map = {}

for s in s1:
    word = ''.join(sorted(list(s)))

    if word in map:
        map[''.join(sorted(list(s)))] += 1
    else:
        map[''.join(sorted(list(s)))] = 1

print(dict(sorted(map.items(), key= lambda map: map[1])))

# {'art': 1, 'ant': 1, 'abt': 2, 'aet': 3}
