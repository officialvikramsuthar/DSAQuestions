nums = [0,0,1,1,1,1,2,3,3]
# nums = [1,1,1,2,2,3]
# nums = [1,2,2,2]



#############
# My Solution
#############


# count = 1
# last_el = nums[0] 
# highest_el = nums[-1]
# unique_count = 1

# for i in range(1, len(nums)):

# 	if last_el == nums[i]:
# 		count += 1

# 		if count > 2:
# 			nums[i] = highest_el
# 		else:
# 			unique_count+=1

# 	else:
# 		last_el = nums[i]
# 		count = 1
# 		unique_count+=1

# nums.sort()
# print(nums)
# print(unique_count)


###############
# Best Solution 
###############


j = 1
for i in range(1, len(nums)):
    if j == 1 or nums[i] != nums[j - 2]:
        nums[j] = nums[i]
        j += 1
print(j)
print(nums)



