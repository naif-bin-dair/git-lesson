import json


name = input("your name: ")
age = int(input("your age: "))
year_of_birth = int(input("your year of birth: "))


try:
    with open("data2.json", "r") as f:
        data = json.load(f)
except:
    data = {}

data[name] = {
    "Age" : age,
    "Year of birth" : year_of_birth
}

with open("data2.json", "w") as f:
    json.dump(data,f,indent=2)