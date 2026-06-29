# '''Fixed Sliding Window

# Used when window size is fixed (k).
# Time Complexity:
# O(n)

# Why not brute force?

# Brute Force:
# Recalculate every window sum.

# Sliding Window:
# Reuse previous window sum.

# O(n*k) -> O(n)

# Use Cases:

# Maximum sum subarray of size k
# Average of subarrays of size k
# Fixed-size window problems

# Example:
# nums=[2,1,5,1,3,2]
# k=3
# Windows:
# [2,1,5]
# [1,5,1]
# [5,1,3]
# [1,3,2]
# Core Idea:
# Instead of recalculating every window sum,
# remove left element and add new right element.

# Formula:
# window_sum = window_sum - leaving_element + entering_element'''

# # nums=[2,1,5,1,3,2]
# # k=3
# # max_sum=sum(nums[:k])
# # window_sum=max_sum   
# # leaving=0
# # adding=k
# # for el in range(k,len(nums)):
# #     window_sum=window_sum-nums[leaving]+nums[adding]
# #     if max_sum<window_sum:
# #         max_sum=window_sum
# #     leaving+=1
# #     adding+=1
# # print(max_sum)
# '''can use both and both are same just variables different'''
# nums=[2,1,5,1,3,2]
# k=3
# max_sum=sum(nums[:k])
# window_sum=max_sum
# for right in range(k,len(nums)):
#     window_sum=window_sum-nums[right-k]+nums[right]
#     '''Why right-k?

# right -> entering element
# right-k -> leaving element

# Example:
# k=3

# right=3
# entering = nums[3]
# leaving = nums[0]'''
#     if max_sum<window_sum:
#         max_sum=window_sum
# print(max_sum)
nums=[1,2,3,4,5]
target=5
left=0
window_sum=0
for right in range(0,len(nums)):
    window_sum+=nums[right]
    while window_sum>=target:
        print(nums[left:right+1])
        window_sum-=nums[left]
        left+=1
       
'''
Variable Sliding Window

Used when window size is NOT fixed.

Main Idea:
Expand window until condition becomes true.
Shrink window until condition becomes false.

Pointers:
left  -> shrink window
right -> expand window

Pattern:

left = 0
window_sum = 0

for right in range(len(nums)):

```
window_sum += nums[right]   # Expand

while condition:

    # update answer

    window_sum -= nums[left]
    left += 1               # Shrink
```

Why while and not if?

Because after shrinking once,
the condition may still be true.

We keep shrinking until the condition becomes false.
    '''