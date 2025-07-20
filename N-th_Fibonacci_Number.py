def fibonacci_dp(n):
    if n <= 1:
        return n

    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

n = int(input("Enter the value of n to find the nth Fibonacci number: "))
print(f"The {n}th Fibonacci number is:", fibonacci_dp(n))
