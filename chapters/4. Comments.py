# "O único comentário verdadeiramente bom é aquele em que você encontrou uma forma para não escreve-lo."

# Add only even numbers to the result
if number % 2 == 0:
    result.append(number)

# Refactoring
def is_even(number):
    return number % 2 == 0

if is_even(number):
    result.append(number)