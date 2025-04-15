# two pointers: start at opposite ends of the array and gradually move towards each other before meeting in the middle
# usage: Should be go to when searching for a pair ( or more ) of elements in the array that meet some criteria
# Runtime: Depends on implementation, but common questions that can use two-points go from O(n^2) to O(n)

arr = [1, 2, 3, 4, 5, 6]
odd_arr = [1,2,3,4,5,6,7]

def two_pointers(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        print(arr[left])
        left += 1
        print(arr[right])
        right -= 1

#two_pointers(arr)
two_pointers(odd_arr)