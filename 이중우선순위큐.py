def solution(operations):
    list = []
    for i in range(len(operations)):
        print(list)
        str = operations[i]
        if str[0] == "I":
            list.append(int(str[2:]))
            list.sort()
        else:
            print(str[2:])
            if not list:
                # print(int(str[2:]))
                if int(str[2:]) == 1 :
                    list.remove(len(list)-1)
                else :
                    list.remove(0)
            else:
                continue
    if not list:
        return [0,0]
    else:
        return [list[0],list[len(list)-1]]