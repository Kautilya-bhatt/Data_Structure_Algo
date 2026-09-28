def first_missing_positive(nums):
    n = len(nums)
    # Place each number in its right place, i.e., nums[i] == i+1
    i = 0
    while i < n:
        cur = nums[i]
        if 1 <= cur <= n and nums[cur - 1] != cur:
            nums[i], nums[cur - 1] = nums[cur - 1], nums[i]
        else:
            i += 1
    # Scan for the first place where the index doesn't match the value
    for i, val in enumerate(nums, 1):
        if val != i:
            return i
    return n + 1

# Example usage
if __name__ == "__main__":
    arr = [3, 4, -1, 1]
    print(first_missing_positive(arr))  # Output: 2
