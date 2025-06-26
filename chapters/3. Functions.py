# My old function: https://github.com/Kecbm/playground-functions
def compareTrue(a, b):
    # your code here
    if a == True and b == True:
        return True
    elif a == False and b == False:
        return False
    else:
        return False


# Refactoring
def are_values_equal(one_value, two_value):
    return one_value == two_value


# My old function: https://github.com/Kecbm/zoo-functions/blob/main/src/calculateEntry.js
def countEntrants(entrants):
    # your code here
    obj = {
        "child": 0,
        "adult": 0,
        "senior": 0,
    }
    for elem in entrants:
        if elem["age"] < 18:
            obj["child"] += 1
        elif elem["age"] >= 18 and elem["age"] < 50:
            obj["adult"] += 1
        elif elem["age"] >= 50:
            obj["senior"] += 1
    return obj


# Refactoring
def countEntrants(entrants):
    counts = {'child': 0, 'adult': 0, 'senior': 0}
    
    for person in entrants:
        age = person['age']
        if age < 18:
            counts['child'] += 1
        elif age < 50:
            counts['adult'] += 1
        else:
            counts['senior'] += 1
            
    return counts