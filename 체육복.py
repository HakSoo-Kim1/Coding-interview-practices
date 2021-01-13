def solution(n, lost, reserve):
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    who_can_borrow = 0
    for lost_person in lost_set:
        if lost_person - 1 in reserve_set:
            reserve_set.remove(lost_person - 1)
            who_can_borrow += 1
        elif lost_person + 1 in reserve_set:
            reserve_set.remove(lost_person + 1)
            who_can_borrow += 1
    return n - len(lost_set) + who_can_borrow