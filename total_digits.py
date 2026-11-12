def count(num):
    if num == 0:
        return 0
    return 1 + count(num//10)
print(count(47589))