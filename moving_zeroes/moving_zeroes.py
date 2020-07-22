'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # start a counter starting at  0
    count = 0
    # loop through the arr
    for item in arr:
        # if any item is 0
        if item == 0:
            # remove the item and increment counter by 1
            arr.remove(item)
            count = count + 1
    # return arr + 0*count
    arr = arr + [0]*count
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
