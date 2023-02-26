import requests
import json

typeOfAnimal = input(
    "Enter the type of the animal you are interested in (cat or dog): ")
amountOfTrivias = int(
    input("Enter the amount of trivias you want to see (min. 11, max. 500): "))


params = {
    "animal_type": typeOfAnimal,
    "amount": amountOfTrivias,
}

r = requests.get("https://cat-fact.herokuapp.com/facts/random", params)

if amountOfTrivias <= 500 and amountOFAnimal > 10:
    try:
        factsAboutCats = r.json()
    except json.decoder.JSONDecodeError:
        print("Wrong format")
    else:
        choisesFactsAboutCats = []
        print(
            "We have selected only verified trivias, which is why there are fewer of them.")
        for fact in factsAboutCats:
            status = fact["status"]
            if status["verified"] == True:
                choisesFactsAboutCats.append(fact["text"])
        for i, fact in enumerate(choisesFactsAboutCats, 1):
            print(i, "." + fact, sep="", end="" + "\n")
else:
    print("You asked for too many or too less trivia, please try again.")
