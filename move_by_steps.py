# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]


# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]

# Without Inplace solution
# i = len(nums) - steps
# count = 1
# els = []

# while count <= steps:
# 	el = nums.pop(i)
# 	els.append(el)
# 	count += 1

# els.extend(nums)
# nums = els
# print(nums)


def move_by_steps(nums, k):
	i = len(nums) - k 
	count = 0

	while count < k:
		el = nums[i]
		temp = nums[count]
		nums[count] = el

		el = nums[count + k]
		nums[i] = el
		nums[count+k] = temp
		i += 1
		count += 1

	print(nums)

nums = [1,2,3,4,5,6,7]
k = 3

print(move_by_steps(nums, k))