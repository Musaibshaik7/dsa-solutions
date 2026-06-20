#day3 two pointers
"""
==============================
TWO POINTER TECHNIQUE
==============================

Definition:
Two pointers use two indices to traverse an array efficiently.
Instead of checking every pair (O(n²)),
we eliminate unnecessary comparisons and often solve the problem in O(n).

When to use:
1. Sorted arrays
2. Pair sum problems
3. Reverse array
4. Palindrome
5. Remove duplicates
6. Opposite ends approaching the center

Golden Rules:

If current sum < target:
    left += 1

Reason:
Need a larger sum.

----------------------------

If current sum > target:
    right -= 1

Reason:
Need a smaller sum.

----------------------------

If current sum == target:

Find one pair:
    Stop

Find all unique pairs:
    left += 1
    right -= 1

----------------------------

Important:

Move a pointer only when its current value has finished its job.

Time Complexity:
Usually O(n)

Space Complexity:
Usually O(1)
"""
arr=[1,2,3,4,5]
left=0
right=len(arr)-1
while(left<right):
    temp=arr[left]
    arr[left]=arr[right]
    arr[right]=temp
    left+=1
    right-=1
print(arr)

arr=[1,2,3,2,1]
left=0
right=len(arr)-1
while(left<right):
    if(arr[left]!=arr[right]):
        print("not palindrome")
        break
    left+=1
    right-=1
else:
    print("palindrome")

arr=[1,2,3,4,5,6,7,8]
target=10
left=0
right=len(arr)-1
while(left<right):
    if(arr[left]+arr[right]==target):
        print([left,right])
        break
    elif(arr[left]+arr[right]<target):
        left+=1
    else:
        right-=1
        
nums = [1, 2, 3, 4, 5, 6, 7, 8]
target = 10
left = 0
right = len(nums) - 1
while left<right:
    if nums[left] + nums[right] == target:
        print(left, right)
        left += 1
        right -= 1  
    elif nums[left] + nums[right] < target:
        left += 1
    else:
        right -= 1