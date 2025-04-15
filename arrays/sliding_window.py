# sliding window: initialize a "window" of some certain size and use that window to iterate through the array
# NOTE: the window size can be either static or dynamic
# usage: when trying to build some sub-array of a certain size
# runtime: generally O(n)
arr = [1,2,3,4,5,6]


def sliding_window(arr):
    window_size = 3
    if len(arr) < window_size:
        return
    for i in range(window_size - 1, len(arr)): # this will slide the window one over each iteration, we do window_size - 1 to correct the arrat indices
        print(f'{arr[i - 2]} {arr[i - 1]} {arr[i]}')


sliding_window(arr)