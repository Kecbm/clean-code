# Page 78
# "Cada linha em branco indica visualmente a separacao entre conceitos. [...]
# Retirar essas linhas em branco, gera um efeito notavelmente obscuro na legibilidade do código."
# "Sem identacao, os programas seriam praticamente initeligiveis para humanos"

def calculate_discount(price, percentage):
    discount = price * (percentage / 100)

    return discount


def apply_discount(price, discount):
    final_price = price - discount

    return final_price


def calculate_savings(original_price, final_price):
    savings = original_price - final_price

    return savings