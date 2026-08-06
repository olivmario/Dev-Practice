def longestSubstring(s, k):
    count = {}
    left = 0
    maxLength = 0
    for right in range(len(s)):
        c = s[right]
        count[c] = count.get(c, 0) + 1
        while len(count) > k:
            leftChar = s[left]
            count[leftChar] -= 1
            if count[leftChar] == 0:
                del count[leftChar]
            left += 1
        maxLength = max(maxLength, right - left + 1)
    return maxLength

s = "abcba"
k = 2
print(longestSubstring(s, k))
