def solution(numbers, target):
    global target_num
    target_num = target

    return dfs(numbers, 0)


# numbers [1 2 3]
# 1 total 1
# 2 total 1 + 2
# 3 total 1 + 2 + 3 return 0
# 3 total 1 + 2 - 3 return 0
# 2 total 1 - 2
# 3 total 1 - 2 + 3 return 1
# 3 total 1 - 2 - 3 return 0

# 1 total -1
# 2 total -1 + 2
# 3 total -1 + 2 + 3 return 0
# 3 total -1 + 2 - 3 return 0
# 2 total -1 - 2
# 3 total -1 - 2 + 3 return 1
# 3 total -1 - 2 - 3 return 0

def dfs(numbers, total):
    answer = 0
    if not numbers:
        if target_num == total: return 1
        return 0
    else:
        answer += dfs(numbers[1:], total + numbers[0])  # +1 numbers [1, 2, 3]
        answer += dfs(numbers[1:], total - numbers[0])  # ([2, 3]) -1) numbers [1, 2, 3]
    return answer