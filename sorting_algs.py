#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 12:27:00 2022

@author: abearden
"""

# All of the below leave nums intact and return a sorted copy of nums.

#####################################################

# Returns a sorted copy of nums.
def mergesort(nums):
    n = len(nums)
    if n == 1:
        return nums
    mid = n//2
    first_half_sorted = mergesort(nums[:mid])
    second_half_sorted = mergesort(nums[mid:])
    return merge(first_half_sorted, second_half_sorted)

# Merges sorted arrays nums1 and nums2.
def merge(nums1, nums2):
    output = []
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            output.append(nums1[i])
            i += 1
        else:
            output.append(nums2[j])
            j += 1
    output.extend(nums1[i:])
    output.extend(nums2[j:])
    return output

#####################################################

import heapq

# A "lazy" version of heapsort, in that it uses the built-in heapq module.
def heapsort_lazy(nums):
    nums_copy = nums.copy()
    heapq.heapify(nums_copy)
    return [heapq.heappop(nums_copy) for _ in range(len(nums_copy))]

# A slightly less lazy version?
def heapsort_lazy2(nums):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
    output = []
    while heap:
        output.append(heapq.heappop(heap))
    return output

# The real deal from scratch, implemented in-place and efficiently, in
# particular, using the bubble-down approach to construct the initial heap.
# Returns nothing.
def heapsort(nums):
    n = len(nums)
    
    # Starting from the lowest parent and working up, heapifies nums.
    for j in range(n // 2 - 1, -1, -1):
        heapify(nums, j, n)
    
    # Iteratively swaps the last element in nums with the top of the heap,
    # then heapifies the non-sorted head of nums.
    for j in range(n-1, -1, -1):
        nums[0], nums[j] = nums[j], nums[0]
        heapify(nums, 0, j)
        
# Transforms the substree of nums[:n] with root nums[i] into a max-heap,
# in-place, assuming that the left and right subtrees of nums[:n] below
# nums[i] are already heaps.    
def heapify(nums, i, n):
    left, right = 2 * i + 1, 2 * i + 2
    
    # Gets: largest = index of max(nums[i], nums[left], nums[right])
    largest = i
    if left < n and nums[i] < nums[left]:
        largest = left
    if right < n and nums[largest] < nums[right]:
        largest = right
    
    # If needed, swaps the root nums[i] with the largest out of it and
    # its children, then moves down the tree and continues.
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        heapify(nums, largest, n)
        
#####################################################

# Sorts nums in-place and returns nothing.
def quicksort(nums, low=0, high=None):
    if not high:
        high = len(nums)
    if high - low > 1:
        p = partition(nums, low, high)
        quicksort(nums, low, p)
        quicksort(nums, p+1, high)
        
# Takes a list nums, and integers low and high, and partitions nums[low:high]
# into three parts: those below the partition element, the partition itself,
# and those above. Works by iterating through the list by i and keeping track of
# three sublists: those already explored and below the partition,
# nums[low:first_high], those already explored and above the partition,
# nums[first_high:i], and those unexplored, nums[i:].
# Returns the index of the partition, which is now in the correct place.

from random import randint

def partition(nums, low, high):
    p = randint(low, high-1) # Randomly sets the partition index p.
    nums[p], nums[high-1] = nums[high-1], nums[p] # Swap the partition to the end.
    p = high - 1 # Reset the partition index to the end.
    first_high = low
    for i in range(low, high - 1):
        if nums[i] < nums[p]:
            nums[i], nums[first_high] = nums[first_high], nums[i]
            first_high += 1
    nums[p], nums[first_high] = nums[first_high], nums[p]
    return first_high

#####################################################

#####################################################

random_list = [randint(1,20) for _ in range(20)]

s = sorted(random_list)
m = mergesort(random_list)
hl = heapsort_lazy(random_list)
hl2 = heapsort_lazy2(random_list)
h = random_list.copy()
heapsort(h)
q = random_list.copy()
quicksort(q)


print('Random list:\n', random_list)
print("Random list after Python's built-in sort:\n", s)
print('Random list after mergesort:\n', m)
print('Random list after heapsort_lazy:\n', hl)
print('Random list after heapsort_lazy2:\n', hl2)
print('Random list after heapsort:\n', h)
print('Random list after quicksort:\n', q)
print('Random list:\n', random_list)
print("All sorted lists match: ", s == m == hl == hl2 == h == q)
