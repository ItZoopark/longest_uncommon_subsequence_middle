def isSubsequence(s1, s2):
    j = 0
    for i in range(len(s1)):
        if j < len(s2) and s1[i] == s2[j]:
            j += 1

    return j == len(s2)


def findLUSlength(strs):
    strs.sort(key=lambda x: -len(x))
    for i in range(len(strs)):
        flag = True
        for j in range(len(strs)):
            if j != i and len(strs[j]) >= len(strs[i]) and isSubsequence(strs[j], strs[i]):
                flag = False
                break

        if flag:
            return len(strs[i])

    return -1


# words = ["aa", "aaa", "aa"]
# words = ["aabbcc", "aabbcc", "c"]
# words = ["aba", "cdc", "eae"]
# words = ["aabbcc", "aabbcc", "cb"]
# words = ["aabbcc", "aabbcc", "c", "e", "aabbcd"]
# print(findLUSlength(words))
print(isSubsequence("aebdc", "abc"))
