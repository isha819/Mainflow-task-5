def permute_string(s):
    def backtrack(chars, left, right, result):
        if left == right:
            result.append(''.join(chars))
        else:
            for i in range(left, right + 1):
                chars[left], chars[i] = chars[i], chars[left]
                backtrack(chars, left + 1, right, result)
                chars[left], chars[i] = chars[i], chars[left]

    result = []
    backtrack(list(s), 0, len(s) - 1, result)
    return result

user_input = input("Enter a string to find its permutations: ")
permutations = permute_string(user_input)
print("All permutations:")
for p in permutations:
    print(p)
