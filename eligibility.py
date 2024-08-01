children = [
    {"name": "Aung", "age": 2, "height": 95},
    {"name": "Khant", "age": 4, "height": 105},
    {"name": "Ko", "age": 3, "height": 110},
    {"name": "Poe", "age": 5, "height": 102},
    {"name": "Ei", "age": 6, "height": 99}
]

eligible_children = [child for child in children if child['age'] > 3 and child['height'] > 100]

print("Eligible children for the fun park:", eligible_children)
