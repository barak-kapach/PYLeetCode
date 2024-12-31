def isHappy(n):
    s = set()

    while n > 1 and n not in s:
        s.add(n)
        res = 0
        while n > 0:
            mod = n % 10
            res += mod ** 2
            n = n // 10
        n = res
    return n == 1
print(isHappy(19))