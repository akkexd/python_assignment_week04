children = [
    {"name": "Aung", "age": 2, "height": 95},
    {"name": "Ko", "age": 4, "height": 105},
    {"name": "Khant", "age": 3, "height": 110},
    {"name": "Ei", "age": 5, "height": 102},
    {"name": "Poe", "age": 6, "height": 99}
]

criteria = lambda child: child['age'] > 3 and child['height'] > 100

eligible_children = [child for child in children if criteria(child)]

print("Eligible children for the fun park:", eligible_children)
