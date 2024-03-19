import array

arr = array.array('i', [1, 3, 4, 5, 6])
target = 11
start = 0 
end = len(arr) -1


while start < end:
    sum = arr[start] + arr[end]
    if sum == target:
        break

    elif sum < target:
        start += 1
    
    else:
        end -= 1

if start == end:
    print("-1")
else:
    print(start, end)
    print(arr[start], arr[end])