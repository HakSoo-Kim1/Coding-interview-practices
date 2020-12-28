import math
def solution(progresses, speeds):
    arr = []
    for i in range(len(progresses)):
        rest_Work = (100 - progresses[i])
        num_Of_RestDays = rest_Work / speeds[i]
        num_Of_RestDays = math.ceil(num_Of_RestDays)
        arr.append(num_Of_RestDays)
    answer = []
    counter = 0
    max = arr[0]
    for i in range(len(arr)):
        if (i == len(arr) -1 ):
            counter = counter + 1
            answer.append(counter)
        else:
            if (max < arr[i+1]):
                counter = counter + 1
                answer.append(counter)
                max = arr[i+1]
                counter = 0
            else :
                counter = counter + 1
    return answer








progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print (solution(progresses,speeds))







