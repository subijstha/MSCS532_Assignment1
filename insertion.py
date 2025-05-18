"""
insertion_sort_desc.py

This script implements the Insertion Sort algorithm to sort a list of numbers
in monotonically decreasing order.

Author: [Your Name]
Course: MSCS532
Assignment: Assignment 1 - Insertion Sort (Descending)
"""

def insertion_sort_desc(arr):
    """
    Sorts the given list in-place in descending order using insertion sort.
    
    Parameters:
        arr (list): List of integers or floats to be sorted.
        
    Returns:
        list: The sorted list in descending order.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Shift elements of arr[0..i-1], that are less than key, to one position ahead
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

def main():
    """
    Demonstrates the use of the insertion_sort_desc function with example input.
    """
    # Sample data
    sample_data = [29, 10, 14, 37, 13, 7, 18]

    print("Original array:")
    print(sample_data)

    # Sort in descending order
    sorted_data = insertion_sort_desc(sample_data)

    print("\nSorted array in descending order:")
    print(sorted_data)

if __name__ == "__main__":
    main()
