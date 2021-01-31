def solution(n, computers):
    connection = [i for i in range(n)]
    for row in range(len(computers)):
        for col in range(len(computers[row])):
            if (computers[row][col] == 1):
                if row == col:
                    continue;
                else:
                    if (connection[row] != connection[col]):
                        smaller = min(row,col)
                        bigger = max(row,col)
                        bigger_temp = connection[bigger]
                        connection[bigger] = connection[smaller]
                        for i in range(len(connection)):
                            if (connection[i] == bigger_temp):
                                connection[i] = connection[smaller]
    connection = list(dict.fromkeys(connection))
    return len(connection)