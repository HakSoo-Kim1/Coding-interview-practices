regular_count = 0
top_down_memoization_fib_memoization_count = 0
bottom_up_memoization_fib_memoization_count = 0

def regular_fib(num):
    global regular_count
    regular_count += 1
    if num <= 1:
        return num
    return regular_fib(num - 2) + regular_fib(num - 1)

def top_down_memoization_fib(num,lookup):
    global top_down_memoization_fib_memoization_count
    top_down_memoization_fib_memoization_count += 1
    if num <= 1:
        return num
    if lookup[num] == 0:
        lookup[num] = top_down_memoization_fib(num-2,lookup) + top_down_memoization_fib(num-1,lookup)
    return lookup[num]

def bottom_up_memoization_fib(n):
    global bottom_up_memoization_fib_memoization_count
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
        bottom_up_memoization_fib_memoization_count += 1
    return dp[n]

num = 20
print("regular non memoization fib")
print(regular_fib(num))
print(regular_count)
lookup = [0]* (num+1)
print("top down memoization fib")
print(top_down_memoization_fib(num,lookup))
print(top_down_memoization_fib_memoization_count)
print("bottom up memoization fib")
print(bottom_up_memoization_fib(num))
print(bottom_up_memoization_fib_memoization_count)








