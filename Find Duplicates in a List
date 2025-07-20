from collections import Counter

def find_duplicates(nums):
    freq = Counter(nums)
    duplicates = [num for num, count in freq.items() if count > 1]
    return duplicates

user_input = input("Enter a list of integers (space-separated): ")
nums = list(map(int, user_input.strip().split()))

duplicates = find_duplicates(nums)

if duplicates:
    print("Duplicate elements are:", duplicates)
else:
    print("No duplicates found.")
