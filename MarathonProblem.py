def solution(participant, completion):
    empty = []
    newParticipant = participant.copy()
    for runner in participant:
        if (runner in completion and runner not in empty):
            newParticipant.remove(runner)
            empty.append(runner)
    return newParticipant[0]
