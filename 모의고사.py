def solution(answers):
    counter = [0,0,0]
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if answers[i] == first[i % len(first)]:
            counter[0] += 1
        if answers[i] == second[i % len(second)]:
            counter[1] += 1
        if answers[i] == third[i % len(third)]:
            counter[2] += 1
    maxValue = max(counter)
    answer = []
    for i in range(len(counter)):
        if (maxValue == counter[i]):
            answer.append(i + 1)
    return answer