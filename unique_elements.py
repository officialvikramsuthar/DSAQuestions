def remove_duplicates(nums=[]):

    length = len(nums)
    count = 0 
    index = 0 

    while length - 1 > count:
        
        if nums[index] == nums[index + 1]:
            nums.pop(index)
        else:
            index += 1

        count += 1
    
    print(nums)

    return len(nums)

nums = [1,1]

print(remove_duplicates(nums=nums))