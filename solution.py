import json
inputFile = "a_example"
outputFile = "a_example.out"

# Taking input
inp = open(inputFile).read().split('\n')

# Defining Global variables
class Vars:
    _, duo, trio, squad = list(map(int,inp[0].strip().split(' ')))


# This is a function to give the pizzas a valid structure
def mapPizzas(line, index):
    list = line.strip().split(' ')[1:]
    # list.sort()
    return {
        "ingredientsCount": len(list),
        "ingredients": list,
        "index": index
    }
pizzas = [mapPizzas(line, index) for index, line in enumerate(inp[1:-1])]
print(json.dumps(pizzas))




# pizzas.sort(key=lambda x: x["ingredientsCount"], reverse=True)

# {indexes, teamType}
submission = []

def packAndSend(pizzasForTeam, teamType):
    indexes = []
    for pizzaForTeam in pizzasForTeam:
        indexes.append(pizzaForTeam["pizza"]["index"])
        pizzas.remove(pizzaForTeam["pizza"])

    submission.append({
        "indexes": indexes,
        "teamType": teamType
    })
    

def calculateForTeam(teamsCount, teamSize, forceSale = False):
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
        # print(json.dumps(pizzasForTeam))
        if len(pizzasForTeam) >= teamSize:
            pizzasForTeam.sort(key=lambda x: x["value"], reverse=True)
            # print(json.dumps(pizzasForTeam))
            packAndSend(pizzasForTeam[0:teamSize], teamSize)
            teamsCount-=1
        else:
            break

    if teamSize == 4:
        Vars.squad = teamsCount
    if teamSize == 3:
        Vars.trio = teamsCount
    if teamSize == 2:
        Vars.duo = teamsCount


print("Calculating for Squad")
calculateForTeam(Vars.squad, 4)
print("Calculating for trio")
calculateForTeam(Vars.trio, 3)
print("Calculating for duo")
calculateForTeam(Vars.duo, 2)


def mapSubmission(sub):
    return ' '.join([str(sub["teamType"]), *list(map(str, sub["indexes"]))])

open(outputFile, "w+").write('\n'.join([str(len(submission)), *list(map(mapSubmission, submission))]))

# print(Vars.duo, Vars.trio, Vars.squad)
print(len(pizzas))