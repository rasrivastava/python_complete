with open("file.txt") as file:
    content = file.read()

print(content)

words_count = {}
each_word = ""

for char in content:
    if char != " " and char != "\n":
        each_word += char
    else:
        if each_word:
            print(each_word)
            if each_word in words_count:
                words_count[each_word] += 1
            else:
                words_count[each_word] = 1
            each_word = ""

# words_count = {"rat": 20, "mat": 25, "cat": 10}

sort_key = sorted(words_count.items(), key=lambda items: items[1])
print(dict(sort_key))

# sort_value = sorted(words_count.items(), key=lambda items: items[0])
# print(dict(sort_value))
