# Find all subarrays from the list where the total of elements is 10. List will always be traversed sequentially
# Example - [1,2,3,2,1,1,2,3,1,2,2]
# Expected output - [1,2,3,2,1,1] [2,1,1,2,3,1] [1,1,2,3,1,2]
# To demonstrate how list is traversed -
# Input list - [1,2,3,2,1,1] [2,3,1,2,2] [2,1,1,2,3,1] [1,1,2,3,1,2]

def find_subarrays_with_sum(arr, target_sum):
    result = []
    n = len(arr)
    for i in range(n):
        current_sum = arr[i]
        subarray = [arr[i]]
        for j in range(i + 1, n):
            current_sum += arr[j]
            subarray.append(arr[j])
            if current_sum == target_sum:
                result.append(subarray[:])  # Append a copy of the current subarray
                break  # Stop expanding further as we found a valid subarray
            elif current_sum > target_sum:
                break  # No need to continue if the sum exceeds the target
    return result

# Example usage
input_list = [1, 2, 3, 2, 1, 1, 2, 3, 1, 2, 2]
target = 10
subarrays = find_subarrays_with_sum(input_list, target)

print("Subarrays with sum 10 are:")
print(subarrays)
