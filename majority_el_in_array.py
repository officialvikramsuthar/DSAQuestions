nums = [2,2,1,1,1,2,2]
counter = {}

for i in range(0, len(nums)):
    count = counter.get(nums[i], 0)
    counter[nums[i]] = count + 1

max_el = 0
max_count = 0 

for key, values in counter.items():
    if values > max_count:
        max_el = key
        max_count = values

print(max_el)