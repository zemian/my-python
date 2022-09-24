nums = [1, 2, 3]
print(nums)
nums.append(4)
print(nums)
nums.remove(3)  # remove value '3', not index
print(nums)
del nums[0]
print(nums)
print(len(nums))
nums.insert(0, 200)
print(nums)
nums.pop()  # remove last element
print(nums)

# list comprehension
nums = [i for i in range(1, 10)]
print(nums)
nums.reverse()
print(nums)

import random
random.shuffle(nums)
print(nums)

nums.sort()
print(nums)

print(5 in nums)
