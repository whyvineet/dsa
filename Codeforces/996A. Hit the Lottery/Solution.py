# https://codeforces.com/problemset/problem/996/A

def solve(n):

    bills = 0
    denominations = [1, 5, 10, 20, 100]

    i = len(denominations) - 1
    while i >= 0:
        if n >= denominations[i]:
            bills += n // denominations[i]
            n %= denominations[i]
        else:
            i -= 1

    return bills

if __name__ == '__main__':
    n = int(input())
    print(solve(n))