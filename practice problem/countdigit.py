def countd(n):
    cnt = 0
    while n != 0:
        n %= 10
        cnt += 1
    return cnt

n = int(input("Enter a number:"))

print(countd(n))