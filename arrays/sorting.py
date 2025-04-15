# sorting: sort the array by some qualifier
# usage: depending on the problem a sorted array can simplify the problem,
# NOTE: this only works if you don't need to maintain order

arr = [1,3,5,7,2,4,6,8]
arr.sort() #sorts in place
print(arr)

arr = [1,3,5,7,2,4,6,8]
new = sorted(arr) # creates new list
print(new)