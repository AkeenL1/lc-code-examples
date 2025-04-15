# Prefix Sum: technique to calculate the sum of subarrays in an array by converting the array to sequential sum
#Note: Suffix sum ios the same just from i - 1 to 0
# Usage: When you need the sum of a particular subarray

arr = [1, 2, 3, 4, 5, 6]


#build prefix sum
def prefix_sum(arr):
    prefix_arr = [0] * (len(arr) + 1)  # has an extra element, 0 at the start
    for i in range(len(arr)):
        prefix_arr[i + 1] = prefix_arr[i] + arr[i]

    print(prefix_arr)
    # for example if we wanted the sum of 3,4,5 or indexes [2,3,4] we can do
    # remember we prefix[0] = 0 not the start
    print(prefix_arr[5] - prefix_arr[2])

prefix_sum(arr)