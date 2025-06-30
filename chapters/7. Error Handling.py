# Page 107
# Sobre bloco try catch, criar no catch:
# "Crie mensagens de erro informativas e as passe com as execoes. Mencione a operacao que falhou e o tipo da falha"


def convert_to_int(value):
    try:
        result = int(value)
        return result
    except ValueError as e:
        error_msg = f"Conversion operation failed: value '{value}' cannot be converted to integer"
        raise ValueError(error_msg) from e
