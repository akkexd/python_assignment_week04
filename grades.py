# Define the list of grades
grades = [55, 70, 65, 40, 90, 85, 50, 77]

# Create a new list with grades 60 and above, applying a 5% bonus
passed_with_bonus = [grade * 1.05 for grade in grades if grade >= 60]

# Print the modified grades
print("Grades after filtering and applying bonus:", passed_with_bonus)

