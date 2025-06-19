def src(a,b):
    for i in range(len(a)):
        if a[i] == b:
            return i
    return -1


a = [1,5,3,7,2]
print(len(a))
target = 7
print("Found at index: ", src(a, target))