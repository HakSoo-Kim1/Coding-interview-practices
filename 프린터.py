from collections import deque
def solution(priorities, location):
    numbersInDescending=[]
    for number in priorities :
        numbersInDescending.append(number)
    numbersInDescending.sort(reverse = True)
    numbersInDescendingQueue = deque(numbersInDescending)
    listWithIndex = []

    for idx, num in enumerate(priorities):
        listWithIndex.append((num,idx))
    listWithIndexQueue = deque(listWithIndex)
    counter = 1
    while (True):

        if (listWithIndexQueue[0][0] == numbersInDescendingQueue[0]):
            if  (listWithIndexQueue[0] == (priorities[location],location)):
                return counter
            else:
                counter = counter + 1
                numbersInDescendingQueue.popleft()
                listWithIndexQueue.popleft()
        else:
            listWithIndexQueue.append(listWithIndexQueue.popleft())





priorities = [1, 1, 9, 1, 1, 1]
print(solution(priorities,0))
