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
# ==========================================
# DAY 4 — SAME DIRECTION & THREE POINTERS
# ==========================================

"""
==========================================
SAME DIRECTION TWO POINTERS
==========================================

Definition:
Both pointers start from the left and move only forward.

Usually:

read  -> scans every element
write -> places useful elements

Pattern:

write = 0

for read in range(len(nums)):

    if current element is useful:
        nums[write] = nums[read]
        write += 1

------------------------------------------

When to use:

1. Remove Element
2. Move Zeroes
3. Remove Duplicates
4. Compress Array
5. Stable Filtering

------------------------------------------

Golden Rules

Read Pointer

✔ Visits every element.
✔ Always moves forward.

------------------------------------------

Write Pointer

✔ Moves ONLY when keeping an element.
✔ Never moves backward.

------------------------------------------

Memory Trick

Read  = Scanner 👀

Write = Painter ✍️

Scanner checks everything.

Painter writes only useful elements.

------------------------------------------

Time Complexity

O(n)

Space Complexity

O(1)
"""



"""
==========================================
THREE POINTERS (Dutch National Flag)
==========================================

Definition:

Used when an array must be divided
into THREE regions.

Most famous problem:

LeetCode 75
Sort Colors

Contains only:

0
1
2

------------------------------------------

Pointers

low
mid
high

Meaning:

low  -> next position for 0

mid  -> current element being checked

high -> next position for 2

------------------------------------------

Rules

If nums[mid] == 0

Swap(mid, low)

low += 1

mid += 1

------------------------------------------

If nums[mid] == 1

Just move

mid += 1

Reason:
1 already belongs in the middle.

------------------------------------------

If nums[mid] == 2

Swap(mid, high)

high -= 1

DO NOT move mid.

Reason:

The element coming from the high side
has NOT been checked yet.

------------------------------------------

Why not move mid after swapping with high?

Because an UNKNOWN element
comes from the right.

We must inspect it first.

------------------------------------------

Memory Trick

0s grow from LEFT.

2s grow from RIGHT.

1s automatically stay in the MIDDLE.

------------------------------------------

Loop

while mid <= high

NOT

for mid in range(...)

Reason:

Sometimes mid moves.

Sometimes it stays.

------------------------------------------

Time Complexity

O(n)

Space Complexity

O(1)
"""


nums=[1,2,0,2,1,0]

left=0
right=len(nums)-1
mid=0
while(mid<=right):
    if(nums[mid]==2):
        nums[mid],nums[right]=nums[right],nums[mid]
        right-=1
    elif(nums[mid]==0):
        nums[mid],nums[left]=nums[left],nums[mid]
        mid+=1
        left+=1
    else:
        mid+=1
   
print(nums)

        
        
            