def solution(routes):
    routes.sort(key = lambda x:x[1])
    print(routes)
    point = routes[0][1]
    answer = 1
    for idx in range(len(routes)):
        if (routes[idx][0] > point):
            point = routes[idx][1]
            answer += 1
    return answer