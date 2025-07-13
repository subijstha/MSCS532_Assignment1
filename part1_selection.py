
import random

# Deterministic Selection (Median of Medians)
def deterministic_select(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k-1]

    sublists = [arr[j:j+5] for j in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist)//2] for sublist in sublists]
    median_of_medians = deterministic_select(medians, len(medians)//2 + 1)

    low = [el for el in arr if el < median_of_medians]
    high = [el for el in arr if el > median_of_medians]
    count = arr.count(median_of_medians)

    if k <= len(low):
        return deterministic_select(low, k)
    elif k > len(low) + count:
        return deterministic_select(high, k - len(low) - count)
    else:
        return median_of_medians

# Randomized Selection (Quickselect)
def randomized_select(arr, k):
    if len(arr) == 1:
        return arr[0]
    pivot = random.choice(arr)
    low = [el for el in arr if el < pivot]
    high = [el for el in arr if el > pivot]
    count = arr.count(pivot)

    if k <= len(low):
        return randomized_select(low, k)
    elif k > len(low) + count:
        return randomized_select(high, k - len(low) - count)
    else:
        return pivot
