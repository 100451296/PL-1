import ply.lex as lex
import ply.yacc as yacc

# Lista de tokens
tokens = (
    "INTEGER",  # Números enteros
    "FLOAT",  # Números reales
    "SCIENTIFIC",  # Notación científica
    "BINARY",  # Números binarios
    "OCTAL",  # Números octales
)

# Definición de las expresiones regulares para los tokens
t_INTEGER = r"\d+"
t_FLOAT = r"(\d*\.\d+)|(\d+\.\d*)"
t_SCIENTIFIC = r"\d+(\.\d*)?[eE][+-]?\d+"
t_BINARY = r"0[bB][01]+"
t_OCTAL = r"0[0-7]+"

# Ignorar espacios y tabulaciones
t_ignore = " \t"


# Regla para manejar el error léxico
def t_error(t):
    print(f'Error léxico: Carácter no reconocido "{t.value[0]}"')
    t.lexer.skip(1)


# Construcción del analizador léxico
lexer = lex.lex()

# Test del analizador léxico
data = "10 420 -12 -999 0.1289 .12 -100.001 10e-1 .1E10 5E2 4e-2 0b101 0B110110 0712 0332 01121"

lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
