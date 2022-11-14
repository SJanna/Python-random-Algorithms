def palindromeIndex(s):
    if s==s[::-1]:
        return -1
    else:
        for i in range(len(s)):
            ns=s[:i] + s[i+1:]
            if ns==ns[::-1]:
                return i
        return -1

q= int(input().strip())

for q_itr in range(q):
    s = input()

    print(palindromeIndex(s))
# 3
# aaab
# baa
# aaa