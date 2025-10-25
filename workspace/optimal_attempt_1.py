import sys

def solve():
    """
    Reads input, solves the maximum subarray sum problem using Kadane's algorithm,
    and prints the result.
    """
    try:
        # Read the size of the array
        n_str = sys.stdin.readline()
        if not n_str:
            return
        n = int(n_str)

        # Read the array elements
        arr_str = sys.stdin.readline()
        if not arr_str:
            return
        arr = list(map(int, arr_str.split()))
    except (IOError, ValueError):
        # Handle potential empty lines or malformed input
        return

    # Kadane's Algorithm
    # The time complexity is O(n) and space complexity is O(1).
    # This is the most efficient approach for this problem.

    # Initialize the maximum sum found so far and the maximum sum ending at the
    # current position with the value of the first element.
    # The constraint 1 <= n guarantees the array is not empty.
    max_so_far = arr[0]
    current_max = arr[0]

    # Iterate through the array starting from the second element.
    for i in range(1, n):
        # The maximum sum of a subarray ending at the current position is either
        # the current element itself (starting a new subarray) or the current
        # element added to the maximum sum of the subarray ending at the previous
        # position (extending the previous subarray).
        current_max = max(arr[i], current_max + arr[i])

        # Update the overall maximum sum if the maximum sum ending at the current
        # position is greater than what we've found so far.
        max_so_far = max(max_so_far, current_max)

    # Print the final result.
    print(max_so_far)

solve()