from stack import Stack

def merge_sort(array, compare):
    if len(array) <= 1:
        return array
    mid = len(array)//2
    left = array[:mid]
    right = array[mid:]
    left = merge_sort(left, compare)
    right = merge_sort(right, compare)
    return merge(left, right, compare)

def merge(left, right, compare):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        
        c = compare(left[i], right[j])
        if c > 0:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result



# data = [2, 10, 44, 33, 5, 100]

# sorted_data = merge_sort(data)

# print(data)
# print(sorted_data)


def compareDes(a, b):
    if a > b:
        return 1
    if a < b:
        return -1
    return 0

def compareAsc(a, b):
    if a < b:
        return 1
    if a > b:
        return -1
    return 0


s1 = Stack()
array = [2,6,7,8,3,9,5,1]
array2 = [] 
# array2 = merge_sort(array, compareDes)
array2 = merge_sort(array, compareAsc)

print(array2)
for i in array2:
    s1.push(i)      


print(f"-> {s1}")