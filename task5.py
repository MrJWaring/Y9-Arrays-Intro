# Create an empty array called names
names = []

# TODO: Use a loop to get 5 names from the user and store them in the array
for i in range(5):
    # Ask the user to enter a name
    name = input("Enter a name: ")
    # TODO: Add the name to the array
    pass

# Initialize a flag for duplicate detection
duplicates_found = False

# TODO: Use nested loops to check for duplicate names
for i in range(len(names)):
    for j in range(i + 1, len(names)):
        # TODO: If a duplicate is found, set duplicates_found to True
        pass

# TODO: Print whether duplicates were found or not
