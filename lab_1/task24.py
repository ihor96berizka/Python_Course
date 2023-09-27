sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
    }

# Rename the key "city" to "location"
sample_dict["location"] = sample_dict.pop("city")

# Print the updated dictionary
print(sample_dict)
