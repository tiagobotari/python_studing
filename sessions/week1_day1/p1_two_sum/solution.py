"""
Problem 1: Two Sum (LeetCode #1)
https://leetcode.com/problems/two-sum/

Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to `target`.

Each input has exactly one solution, and you may not use the same element twice.

Example:
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
"""

"""
def two_sum(nums: list[int], target: int) -> list[int]:
    # Brute force implementation. 
    if len(nums) == 0:
        return []
    
    # (nums list[int], target: int) -> list[int]:
    for i, val1 in enumerate(nums):
        for j, val2 in enumerate(nums):
          if val1 + val2 == target and i!=j:
              return [i, j]  
    return []
"""

# def two_sum(nums: list[int], target: int) -> list[int]:
#     """
#      Hash map implementation. Iterate only once in the array. 
#      Time complexity: O(n)
#      Space complexity: O(n)
#      Key takeaway: Hash maps turn O(n^2) lookups into O(n). 
#      This pattern appears constantly.
#     """
#     rest_tested = {}  # {Value: index}
#     for i, num_i in enumerate(nums):
#         if num_i in rest_tested:
#             return [rest_tested[num_i], i]
#         rest_tested[target - num_i] = i
#     return []
 
# def two_sum(nums: list[int], target: int) -> list[int]:
#     seen_complement = {}
#     for i, num_i in enumerate(nums):
#         complement = target - num_i
#         try:
#             return [seen_complement[num_i], i]
#         except KeyError:
#             seen_complement[complement] = i   
#     return []


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Returns the index of the numbers from a list that 
    sum to target value. 
    Args:
        nums (list[int]): _description_
        target (int): _description_

    Returns:
        list[int]: _description_
    """
    
    seen_num = dict()
    for i, num in enumerate(nums):
        needed_complement = target - num
        if needed_complement in seen_num:
            return [seen_num[needed_complement], i]
        seen_num[num] = i
    return []