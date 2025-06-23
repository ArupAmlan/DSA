s = " hey, i'm good"
d = ""
for i in s:
    if i not in (",","'"," "):
        d+= i

print(d)
c = d[::-1]
if c==d:
    return True
else:
    return False