def num_decodings(s):
    if not s or s[0] == '0':
        return 0

    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        one_digit = int(s[i-1 : i])
        if one_digit >= 1:
            dp[i] += dp[i-1]
        two_digits = int(s[i-2 : i])
        if 10 <= two_digits <= 26:
            dp[i] += dp[i-2]

    return dp[n]

#Test
print(num_decodings("111")) #(aaa, ak, ka)
print(num_decodings("12")) #(ab, l)
