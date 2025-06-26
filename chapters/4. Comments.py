# "O único comentário verdadeiramente bom é aquele em que você encontrou uma forma para não escreve-lo."- page 55

# Add only even numbers to the result
if number % 2 == 0:
    result.append(number)

# Refactoring
def is_even(number):
    return number % 2 == 0

if is_even(number):
    result.append(number)


# TODO

# Page 66
# "Troque a tentacao para criar ruidos pela determinacao para limpar seu codigo. Voce percebera que isso lhe tornara um programador melhor e mais feliz."

# Old code my here
# And the refactor here