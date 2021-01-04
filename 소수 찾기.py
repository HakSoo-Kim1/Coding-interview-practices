import itertools
def solution(numbers):
    answer = 0
    character_list = [character for character in list(numbers)]
    possible_cases = set([])
    for r in range(1,len(character_list) + 1):
        temp = list(itertools.permutations(character_list,r))
        for each_tuple in temp:
            str = ""
            for letters_in_tuples in each_tuple:
                str += letters_in_tuples
            possible_cases.add(int(str))
    for case in possible_cases:
        if (is_prime(case)):
            answer += 1
    return answer

def is_prime(case):
    if case >= 2:
        for i in range(2, case):
            if (case % i) == 0:
                return False
        return True
    else:
        return False