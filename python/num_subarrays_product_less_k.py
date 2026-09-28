def num_subarray_product_less_than_k(nums, k):
    if k <= 1:
        return 0
    prod = 1
    left = 0
    count = 0
    for right, val in enumerate(nums):
        prod *= val
        while prod >= k and left <= right:
            prod //= nums[left]
            left += 1
        count += right - left + 1
    return count

# Example usage
if __name__ == '__main__':
    arr = [10, 5, 2, 6]
    k = 100
    print(num_subarray_product_less_than_k(arr, k))  # Expected output: 8