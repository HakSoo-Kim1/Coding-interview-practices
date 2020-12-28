def solution(prices):
    answer = []
    for i in range(len(prices)):
        counter = 0
        for j in range(i,len(prices)):
            if prices[i] > prices[j] or j == len(prices) - 1:
                break
            else :
                counter =counter + 1
        answer.append(counter)
    return answer