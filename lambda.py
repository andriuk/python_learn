people = [
    {"name": "Гаррі", "house": "Гриффиндор"},
    {"name": "Чо", "house": "Рейвенклов"},
    {"name": "Драко", "house": "Слизерин"}
]

people.sort(key=lambda person: person["name"])

print(people)
