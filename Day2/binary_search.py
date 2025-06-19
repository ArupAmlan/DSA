def bsrc(a,t):
    low = 0
    high = len(a) - 1
    while low<= high:
        mid = (low + high) // 2
        print(mid)
        if a[mid] == t:
            return mid
        elif a[mid] < t:
            low = mid + 1
        else:
            high = mid - 1
    return -1

a = [1,3,5,7,9]
# a.sort()
t = 9
print("Found at index: ", bsrc(a,t))