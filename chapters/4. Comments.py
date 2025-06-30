# “The only truly good comment is the one you found a way not to write.”

# Add only even numbers to the result
if number % 2 == 0:
    result.append(number)

# Refactoring
def is_even(number):
    return number % 2 == 0

if is_even(number):
    result.append(number)