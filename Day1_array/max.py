a = [2,3,7,9,1,5]
print(f"List: {a}")

b = a[0]

for i in a:
    if i > b:
        b = i

print(f"max number is {b}")