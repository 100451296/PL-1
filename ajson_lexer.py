import ply.lex as lex

# Lista de tokens
tokens = (
    "FLOAT",  # Numeros reales
    "INTEGER",  # Numeros enteros
    "SCIENTIFIC",  # Notacion cientifica
    "BINARY",  # Numeros binarios
    "OCTAL",  # Numeros octales
    "HEX",  # Numeros hexadecimales
    "STRING",  # Cadena sin comillas (solo para claves)
    "QUOTED_STRING",  # Cadena con comillas
    "TRUE",  # Booleano True (caracter reservado)
    "FALSE",  # Booleano False (caracter reservado)
    "NULL",  # NULL (caracter reservado)
    "EQUAL",  # Operador ==
    "GRATER",  # Operador >
    "GRATER_EQUAL",  # Operador >=
    "LOWER",  # Operador <
    "LOWER_EQUAL",  # Operador <=
    "OPEN_BRACE",  # Llave apertura {
    "CLOSE_BRACE",  # Llave cierre }
    "COLON",  # Dos puntos :
    "COMMA",  # Coma ,
    "OPEN_BRACKET", # Corchete apertura [
    "CLOSE_BRACKET", # Corchete cierre ]
)


# Expresiones regulares para los tokens
def t_SCIENTIFIC(t):
    r"(\d+(\.\d*)?|\.\d+)[eE][+-]?\d+"
    t.value = float(t.value)
    return t


def t_BINARY(t):
    r"0[bB][01]+"
    t.value = int(t.value, 2)
    return t


def t_OCTAL(t):
    r"0[0-7]+"
    t.value = int(t.value, 8)
    return t


def t_HEX(t):
    r"0[xX][0-9A-F]+"
    t.value = int(t.value, 16)
    return t


def t_STRING(t):
    r"(?!TR\b|tr\b|FL\b|fl\b|NULL\b|null\b)[_a-zA-Z][_a-zA-Z0-9]*\b"
    return t


def t_QUOTED_STRING(t):
    r'"([^"\n]*)?"'
    t.value = t.value[1:-1]
    return t


def t_TRUE(t):
    r"TR|tr"
    t.value = True
    return t


def t_FALSE(t):
    r"FL|fl"
    t.value = False
    return t


def t_NULL(t):
    r"NULL|null"
    t.value = None
    return t


def t_EQUAL(t):
    r"=="
    return t


def t_GRATER_EQUAL(t):
    r">="
    return t


def t_LOWER_EQUAL(t):
    r"<="
    return t


def t_GRATER(t):
    r">"
    return t


def t_LOWER(t):
    r"<"
    return t


def t_OPEN_BRACE(t):
    r"{"
    return t


def t_CLOSE_BRACE(t):
    r"}"
    return t


def t_COLON(t):
    r":"
    return t


def t_COMMA(t):
    r","
    return t


def t_OPEN_BRACKET(t):
    r"\["
    return t


def t_CLOSE_BRACKET(t):
    r"]"
    return t 


def t_FLOAT(t):
    r"-?(\d*\.\d+)|(\d+\.\d*)"
    t.value = float(t.value)
    return t


def t_INTEGER(t):
    r"-?\d+"
    t.value = int(t.value)
    return t


# Ignorar espacios, tabulaciones y saltos de línea
t_ignore = " \t\n"


# Regla para manejar el error léxico
def t_error(t):
    print(f'Error léxico: Carácter no reconocido "{t.value[0]}"')
    t.lexer.skip(1)


# Construcción del analizador léxico
scanner = lex.lex()

if __name__ == "__main__":
    data = "[]"
    scanner.input(data)
    while True:
        tok = scanner.token()
        if not tok:
            break  # No hay más tokens
        print(tok)