def solution(n, costs):
    lst = [i for i in range(n)]
    costs.sort(key = lambda x: x[2])
    answer = 0
    print(costs)
    for i in range(len(costs)):
        if (lst[costs[i][0]] != lst[costs[i][1]]):
            answer += costs[i][2]
            temp_max = lst[max(costs[i][0],costs[i][1])]
            lst[costs[i][0]] = lst[min(costs[i][0],costs[i][1])]
            lst[costs[i][1]] = lst[min(costs[i][0],costs[i][1])]
            for idx in range(len(lst)):
                if lst[idx] == temp_max:
                    lst[idx] = min(costs[i][0],costs[i][1])
        print(lst)
        print(answer)
    return answer