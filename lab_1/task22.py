def delete_key(key, sample_dict):
    if key in sample_dict:
        del sample_dict[key]
    else:
        print(key, "don`t found")


our_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
    }

delete_key("name", our_dict)
delete_key("salary", our_dict)
delete_key("red", our_dict)

print(our_dict)
