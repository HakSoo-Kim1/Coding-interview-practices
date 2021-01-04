def solution(citations):
    h = max(citations)
    while True:
        over = 0
        small = 0
        for i in range(len(citations)):
            if (citations[i] >= h):
                over += 1
            else:
                small += 1
        if (over == h):
            return h
        h -= 1
