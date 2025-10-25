import sys

def solve():
    """
    This function reads the input, finds the maximum subarray sum using a brute force approach,
    and prints the result.
    """
    try:
        # Read the size of the array
        n_str = sys.stdin.readline()
        if not n_str:
            return
        n = int(n_str)
        
        # Read the array elements
        line = sys.stdin.readline()
        if not line:
            return
        arr = list(map(int, line.split()))
    except (IOError, ValueError):
        return

    # Initialize max_sum with a very small number to handle cases with all negative numbers.
    # The sum of the first element is a safe starting point if n >= 1.
    max_so_far = float('-inf')

    # Iterate through all possible starting points of a subarray
    for i in range(n):
        # Iterate through all possible ending points of a subarray
        for j in range(i, n):
            # Calculate the sum of the current subarray arr[i...j]
            current_sum = 0
            for k in range(i, j + 1):
                current_sum += arr[k]
            
            # Update the maximum sum found so far
            if current_sum > max_so_far:
                max_so_far = current_sum
    
    # Print the final result
    print(max_so_far)

solve()