def findMinValue(arr, n):
    # Find the sum of the array elements
    sum = 0
    for i in range(n):
        sum += arr[i]

    # Return the required value
    return (sum // n) + 1


# Driver code
arr = [4, 2, 1, 10, 6]
n = len(arr)
print(findMinValue(arr, n))