#https://leetcode.com/problems/remove-element/description/
def remove_el(nums, num):
    index = 0 
    length = len(nums)

    for i in range(length):
        if nums[index] == num:
            nums.pop(index)
        else:
            index += 1

    return len(nums)

print(remove_el([0,1,2,2,3,0,4,2], 2))
