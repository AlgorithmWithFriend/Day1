def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(participant) - 1):
        if completion[i] != participant[i]:
            return participant[i]
    return participant[-1]


participant_1 = ["leo", "kiki", "eden"]
participant_2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
participant_3 = ["mislav", "stanko", "mislav", "ana"]

completion_1 = ["eden", "kiki"]
completion_2 = ["josipa", "filipa", "marina", "nikola"]
completion_3 = ["stanko", "ana", "mislav"]

print(solution(participant_1, completion_1))
print(solution(participant_2, completion_2))
print(solution(participant_3, completion_3))