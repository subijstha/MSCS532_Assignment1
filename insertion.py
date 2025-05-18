"""
insertion_sort_desc.py

Final version of the Insertion Sort algorithm that sorts a list in monotonically
descending order. This version allows user input and includes input validation.

Author: [Your Name]
Course: MSCS532
Assignment: Assignment 1 - Insertion Sort (Descending)
"""

from typing import List

def insertion_sort_desc(arr: List[int]) -> List[int]:
    """
    Sorts a list of integers in descending order using the insertion sort algorithm.

    Parameters:
        arr (List[int]): The list of integers to sort.

    Returns:
        List[int]: The sorted list in descending order.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def main():
    """
    Main function that gets input from the user, sorts it, and prints the result.
    """
    user_input = input("Enter numbers separated by spaces: ").strip()

    if not user_input:
        print("No input provided.")
        return

    try:
        numbers = list(map(int, user_input.split()))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return

    print("\nOriginal list:")
    print(numbers)

    sorted_numbers = insertion_sort_desc(numbers)

    print("\nSorted list in descending order:")
    print(sorted_numbers)

if __name__ == "__main__":
    main()
