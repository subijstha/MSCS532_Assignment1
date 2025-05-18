def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements smaller than key to the right
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage
if __name__ == "__main__":
    arr = [5, 2, 9, 1, 5, 6]
    print("Original:", arr)
    sorted_arr = insertion_sort_desc(arr)
    print("Sorted (descending):", sorted_arr)
