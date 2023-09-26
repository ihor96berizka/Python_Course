employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

value = {employee: defaults.copy() for employee in employees}

print(value)