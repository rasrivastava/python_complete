word1 = "horse"
word2 = "ros"

def solve(word1, word2, i, j):
    if (len(word1) == i):
        return len(word2) - j
    if (len(word2) == j):
        return len(word1) - i
    
    ans = 0

    if (word1[i] == word2[j]):
        ans = 0 + solve(word1, word2, i+1, j+1)
    else:
        insertion_opr = 1 + solve(word1, word2, i+1, j+1)
        update_opr = 1 + solve(word1, word2, i+1, j)
        delete_opr = 1 + solve(word1, word2, i, j+1)

        ans = min(insertion_opr, min(update_opr, delete_opr))
    
    return ans

i = 0
j = 0
ans = solve(word1, word2, i, j)
print(ans)
