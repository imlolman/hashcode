
inputFile = "c_many_ingredients.in"
outputFile = "c_many_ingredients.out"

inp = open(inputFile).read().split('\n')

_, duo, trio, squad = list(map(int,inp[0].strip().split(' ')))

# print(duo, trio, squad)

def mapPizzas(line, index):
    list = line[1:].strip().split(' ')
    list.sort()
    return {
        "ingredientsCount": len(list),
        "ingredients": list,
        "index": index
    }

pizzas = [mapPizzas(line, index) for index, line in enumerate(inp[1:-1])]
pizzas.sort(key=lambda x: x["ingredientsCount"], reverse=True)
# print(pizzas)

# {indexes, teamType}
submission = []

def packAndSend(pizzasForTeam, teamType):
    indexes = []
    for pizzaForTeam in pizzasForTeam:
        # adding None to ignore the pizza in future
        indexes.append(pizzaForTeam["pizza"]["index"])
        pizzas.remove(pizzaForTeam["pizza"])

    submission.append({
        "indexes": indexes,
        "teamType": teamType
    })
    

def calculateForTeam(teamsCount, teamSize):
    while teamsCount:
        # Unique items for a team
        unique = []

        # {pizzas, value}
        pizzasForTeam = []

        for pizza in pizzas:
            value = 0
            for ingredient in pizza["ingredients"]:
                if ingredient not in unique:
                    value += 1
                    unique.append(ingredient)
            if value != 0:
                pizzasForTeam.append({
                    "pizza": pizza,
                    "value": value
                })
        if len(pizzasForTeam) >= teamSize:
            pizzasForTeam.sort(key=lambda x: x["value"], reverse=True)
            packAndSend(pizzasForTeam[0:teamSize], teamSize)
            teamsCount-=1
        else:
            break
    print("packed for 1 team")

print("Calculating for Squad")
calculateForTeam(squad, 4)
print("Calculating for trio")
calculateForTeam(trio, 3)
print("Calculating for duo")
calculateForTeam(duo, 2)


def mapSubmission(sub):
    return ' '.join([str(sub["teamType"]), *list(map(str, sub["indexes"]))])

open(outputFile, "w+").write('\n'.join([str(len(submission)), *list(map(mapSubmission, submission))]))

