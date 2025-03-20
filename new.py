arr = [64, 34, 25, 12, 22, 11, 90]

# Perform Bubble Sort
n = len(arr)
print(n)
for i in range(n):
    for j in range(0, n - i - 1):
        # Swap if the element found is greater than the next element
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(arr)

# Print the sorted list
print("Sorted array is:", arr)