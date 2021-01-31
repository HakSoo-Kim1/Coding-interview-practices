def solution(triangle):
    sum_lst = [[] for _ in range(len(triangle))]
    for i in range(len(triangle)):
        for j in range(i + 1):
            sum_lst[i].append(-1)
    sum_lst[0][0] = triangle[0][0]
    for i in range(len(triangle) - 1):
        for j in range(len(triangle[i+1])-1):
            print((i,j))
            if (sum_lst[i+1][j] <= triangle[i+1][j] + sum_lst[i][j]):
                sum_lst[i+1][j] = sum_lst[i][j] + triangle[i+1][j]
            print(sum_lst)
            if (sum_lst[i+1][j+1] < triangle[i+1][j+1] + sum_lst[i][j]):
                sum_lst[i + 1][j + 1] = triangle[i+1][j+1] + sum_lst[i][j]
            print(sum_lst)
    return max(sum_lst[-1])
triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

print(solution(triangle))

# print(sum_lst)