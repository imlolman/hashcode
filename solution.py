
inputFile = "b_little_bit_of_everything.in"
outputFile = "b_little_bit_of_everything.out"

inp = open(inputFile).read().split('\n')

_, duo, trio, squad = list(map(int,inp[0].strip().split(' ')))

# print(duo, trio, squad)

pizzas = list(map(lambda x: x[1:].strip().split(' '), inp[1:-1]))

# print(pizzas)

# {indexes, teamType}
submission = []

def packAndSend(pizzasForTeam, teamType):
    indexes = []
    for pizzaForTeam in pizzasForTeam:
        # adding None to ignore the pizza in future
        pizzas[pizzaForTeam["index"]].append(None)
        indexes.append(pizzaForTeam["index"])

    submission.append({
        "indexes": indexes,
        "teamType": teamType
    })
    

while squad:
    teamSize = 4
    # Unique items for a team
    unique = []

    # {pizzaId, value}
    pizzasForTeam = []

    for index,pizza in enumerate(pizzas):
        value = 0
        if None in pizza:
            continue
        for item in pizza:
            if item not in unique:
                value += 1
                unique.append(item)
        if value != 0:
            pizzasForTeam.append({
                "index": index,
                "value": value
            })
    if len(pizzasForTeam) >= teamSize:
        pizzasForTeam.sort(key=lambda x: x["value"], reverse=True)
        packAndSend(pizzasForTeam[0:teamSize], teamSize)
        squad-=1
    else:
        break

while trio:
    teamSize = 3
    # Unique items for a team
    unique = []

    # {pizzaId, value}
    pizzasForTeam = []

    for index,pizza in enumerate(pizzas):
        value = 0
        if None in pizza:
            continue
        for item in pizza:
            if item not in unique:
                value += 1
                unique.append(item)
        if value != 0:
            pizzasForTeam.append({
                "index": index,
                "value": value
            })
    if len(pizzasForTeam) >= teamSize:
        pizzasForTeam.sort(key=lambda x: x["value"], reverse=True)
        trio-=1
        packAndSend(pizzasForTeam[0:teamSize], teamSize)
    else:
        break
    

while duo:
    teamSize = 2
    # Unique items for a team
    unique = []

    # {pizzaId, value}
    pizzasForTeam = []

    for index,pizza in enumerate(pizzas):
        value = 0
        if None in pizza:
            continue
        for item in pizza:
            if item not in unique:
                value += 1
                unique.append(item)
        if value != 0:
            pizzasForTeam.append({
                "index": index,
                "value": value
            })
    if len(pizzasForTeam) >= teamSize:
        pizzasForTeam.sort(key=lambda x: x["value"], reverse=True)
        duo-=1
        packAndSend(pizzasForTeam[0:teamSize], teamSize)
    else:
        break

def mapSubmission(sub):
    return ' '.join([str(sub["teamType"]), *list(map(str, sub["indexes"]))])

    

open(outputFile, "w+").write('\n'.join([str(len(submission)), *list(map(mapSubmission, submission))]))

