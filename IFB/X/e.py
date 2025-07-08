_, _ = input().split()

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

listf = []

i1 = 0; i2 = 0

ult_elem = 0

while i1 != len(list1) and i2 != len(list2):
    if list1[i1] == ult_elem:
        i1 += 1
        continue
    if list2[i2] == ult_elem:
        i2 += 1
        continue
    if list1[i1] == list2[i2]:
        listf.append(list1[i1])
        ult_elem = list1[i1]
        i1 += 1
        i2 += 1
    elif list1[i1] < list2[i2]:
        listf.append(list1[i1])
        ult_elem = list1[i1]
        i1 += 1
    else:
        listf.append(list2[i2])
        ult_elem = list2[i2]
        i2 += 1

while i1 != len(list1):
    if list1[i1] != ult_elem:
        listf.append(list1[i1])
        ult_elem = list1[i1]
        i1 += 1

while i2 != len(list2):
    if list2[i2] != ult_elem:
        listf.append(list2[i2])
        ult_elem = list2[i2]
        i2 += 1

print(" ".join(list(map(str, listf))))