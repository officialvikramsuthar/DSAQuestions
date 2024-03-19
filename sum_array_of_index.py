# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

 # Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# Example 2:

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
# Example 3:

# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].


# numbers = [0, 0, 0 , 0, 0 , 0 , 0, 0, 0, 0, 0, 0, 2, 3, 9, 9, 9, 9]
# target = 5
# numbers = [-1,0]
# target = -1

# numbers = [2,3,4]
# target = 6

numbers = [2,7,11,15]
target = 9


def sum_of_to_in_array(numbers = numbers, target = target):
	index = 0
	j = len(numbers) - 1

	while index < j:
		add = numbers[index] + numbers[j]

		if add == target:
			return [index + 1, j+1]

		elif add > target:
			j -= 1
		else:
			index += 1

print(sum_of_to_in_array())

