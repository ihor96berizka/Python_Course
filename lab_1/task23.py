sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
    }

# Ask the user to enter a key
key = input("Enter a key to check: ")

# Check if the key exists in the dictionary
if key in sample_dict:
    print(f"The key '{key}' exists in the dictionary.")
else:
    print(f"The key '{key}' was not found in the dictionary.")
