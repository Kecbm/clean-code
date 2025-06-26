# TODO: Texto e imagem para postar no LinkedIn

# Page 78
# "Cada linha em branco indica visualmente a separacao entre conceitos. [...] Retirar essas linhas em branco, gera um efeito notavelmente obscuro na legibilidade do código."
# "Sem identacao, os programas seriam praticamente initeligiveis para humanos"

def calculate_discount(price, discount_percent):
    discount_amount = price * (discount_percent / 100)
    return discount_amount


def calculate_tax(price, tax_percent):
    tax_amount = price * (tax_percent / 100)
    return tax_amount


def calculate_final_price(original_price, discount_percent, tax_percent):
    discount = calculate_discount(original_price, discount_percent)
    price_after_discount = original_price - discount
    final_price = price_after_discount + calculate_tax(price_after_discount, tax_percent)
    return final_price