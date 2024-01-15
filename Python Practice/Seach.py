l = [4, 1, 3, 2]
search = int(input("Enter the element to be searched: "))
case = 0
for e in l:
    if search == e:
        case = 1
        break
    else:
        case = 0

if case == 1:
    print("Element Found")
else:
    print("Element Not Found")
