# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        # Find the next smallest index
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        
        # Swap the values
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Algorithm should stop if no swap occurs
    # The last item in the list is going to be the largest after the first
    # iteration. We can shorten the list by n-1 each time.
    iters = 0 # Floor iterations for list length
    does_swap = True # Proc the first iteration
    while does_swap:
        does_swap = False # Set the base case
        # Iterate through minimum array (n) - 1
        for i in range(len(arr) - iters - 1):
            if arr[i] > arr[i+1]: # Check if current is larger than the next
                # Swap the values
                arr[i], arr[i+1] = arr[i+1], arr[i]
                does_swap = True # Reset for another iteration
        iters = iters + 1 # Shorten our list by 1

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
