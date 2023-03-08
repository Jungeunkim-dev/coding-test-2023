def solution(participant, completion):
    runners = {}
    for person in participant:
        if person not in participant:
            runners[person] = 1
        else:
            runners[person] += 1

    for person in completion:
        if person not in runners or runners[person] == 0:
            return person
        else:
            runners[person] -= 1
