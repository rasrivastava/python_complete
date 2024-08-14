s1 = "RAHUL"

def reverse(s1, start, end):
    if (start >= end):
        return

    s1 = list(s1)
    
    s1[start], s1[end] = s1[end], s1[start]
    reverse(s1, start+1, end-1)
    return "".join(s1)


start = 0
end = len(s1) - 1
result = reverse(s1, start, end)
print(result)
