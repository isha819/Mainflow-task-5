def length_of_LIS(nums):
    n = len(nums)
    if n == 0:
        return 0

    # Initialize the dp array
    dp = [1] * n

    # Build the dp array
    for i in range(1, n):
        for j in range(0, i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

user_input = input("Enter a list of integers (space-separated): ")
nums = list(map(int, user_input.strip().split()))

length = length_of_LIS(nums)
print("Length of the Longest Increasing Subsequence is:", length)
