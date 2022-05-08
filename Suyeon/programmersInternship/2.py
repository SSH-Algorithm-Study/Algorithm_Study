import collections
import heapq

def solution(rooms, target):
    answer = []
    roomByPerson = collections.defaultdict(list)
    personByRoom = collections.defaultdict(list)
    howManySeat = collections.defaultdict(list)

    def distance(person):
        dis = float('inf')
        for r in roomByPerson[person]:
            dis = min(dis, abs(target - r))

        return dis

    # 기록
    for room in rooms:
        roomNumber, people = room[1:].split("]")
        people = people.split(",")
        for name in people:
            personByRoom[int(roomNumber)].append(name)
            roomByPerson[name].append(int(roomNumber))

    black_list = personByRoom[target]


    for person in roomByPerson.keys():
        if person not in black_list:
            howManySeat[len(roomByPerson[person])].append(person)

    sortHowmany = sorted(howManySeat.keys())


    for num in sortHowmany:
        candidate = howManySeat[num]
        personBydistance = collections.defaultdict(list)
        for c in candidate:
            personBydistance[distance(c)].append(c)

        keys = sorted(personBydistance.keys())

        for key in keys:
            sorted_key = sorted(personBydistance[key])
            for p in sorted_key:
                answer.append(p)




    return answer


print(solution(["[403]James", "[404]Azad,Louis,Andy", "[101]Azad,Guard"], 403))
