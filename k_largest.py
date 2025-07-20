def k_largest_sort(nums, k):
    nums.sort(reverse=True)
    return nums[:k]

user_input = input("Enter a list of integers (space-separated): ")
nums = list(map(int, user_input.strip().split()))

k = int(input("Enter the value of k: "))

if k <= 0 or k > len(nums):
    print("Invalid value of k.")
else:
    result = k_largest_sort(nums, k)
    print(f"The {k} largest elements are:", result)
