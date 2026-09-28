def max_subarray_one_deletion(nums):
    n = len(nums)
    if n == 0:
        return 0
    # forward max subarray sum ending at each index
    fwd = [0] * n
    fwd[0] = nums[0]
    for i in range(1, n):
        fwd[i] = max(nums[i], fwd[i - 1] + nums[i])
    # backward max subarray sum starting at each index
    bwd = [0] * n
    bwd[-1] = nums[-1]
    for i in range(n - 2, -1, -1):
        bwd[i] = max(nums[i], bwd[i + 1] + nums[i])
    # best without deletion
    ans = max(fwd)
    # consider deleting each element (except first and last) and combine
    for i in range(1, n - 1):
        ans = max(ans, fwd[i - 1] + bwd[i + 1])
    return ans

if __name__ == "__main__":
    # Example usage
    arr = [1, -2, 0, 3]
    print(max_subarray_one_deletion(arr))  # Output: 4 (delete -2)
