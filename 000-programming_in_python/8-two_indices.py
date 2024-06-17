# Question 8:
# Write a Python function in which when given a list of integers and an integer target, returns indices 
# of the two numbers such that they add up to target. You may assume that each input would have 
# exactly one solution, and you may not use the same element twice. You can return the answer in 
# any order. The function signature is as follows: def two_indices(nums, target)

def two_indices(nums, target):
    num_dict = {} #to store those indices that make target
    for i, num in enumerate(nums):
        if num in num_dict:
            return [num_dict[num], i]
        else:
            num_dict[target - num] = i
    return []

#test function
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 18 
    print(two_indices(nums,target))       