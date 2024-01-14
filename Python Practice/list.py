#  list is like array []
num = [1, 2, 3, 4, "yash"]
print(num)

print(num[-1])  # yash

num.append("Jay")
print(num)

num.extend([22, 23])
print(num)

num.insert(0, "arora")
print(num)

num.remove("yash")
print(num)

num.pop()
print(num)

print(len(num))

for x in num:
    print(x)

for x in range(0, 9):
    print(x)

l = [2, 1, 3, 0]
l.sort()
print(l)

l.reverse()
print(l)

new_l = sorted(l)
print(new_l)

print(211 in num)  # False

print(221 not in num)

new=l
print(new)
