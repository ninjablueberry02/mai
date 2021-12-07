list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
 def merge(1: list, 2: list):
    len1 = len(1)
    len2 = len(2)
    if len(1) > len2:
        1, 2 = 2, 1
        len1, len2 = len1, len2
 
    while i <= len1:
        if i == len1:
            listn = listn + 2[j:len2]
            return listn
        elif j == len2:
            listn = listn + 1[i:len1]
            return listn
        if 1[i] < 2[j]:
            listn.append(1[i])
            i += 1
        elif 1[i] == 2[j]:
            listn.append(1[i])
            listn.append(2[j])
            i += 1
            j += 1
        else:
            listn.append(2[j])
            j += 1
 
 
print(*merge(list1, list2))
