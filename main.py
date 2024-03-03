import ply.lex as lex
import ply.yacc as yacc

# Lista de tokens
tokens = (
    "INTEGER",  # Numeros enteros
    "FLOAT",  # Numeros reales
    "SCIENTIFIC",  # Notacion cientifica
    "BINARY",  # Numeros binarios
    "OCTAL",  # Numeros octales
    "HEX",  # Numeros hexadecimales
    "STRING",  # Cadena sin comillas (solo para claves)
    "QUOTED_STRING",  # Cadena con comillas
    "TRUE",  # Booleano True (caracter reservado)
    "FALSE",  # Booleano False (caracter reservado)
    "NULL",  # NULL (caracter reservado)
)

# Definición de las expresiones regulares para los tokens
t_INTEGER = r"-?\d+"
t_FLOAT = r"-?(\d*\.\d+)|(\d+\.\d*)"
t_SCIENTIFIC = r"(\d+(\.\d*)?|\.\d+)[eE][+-]?\d+"
t_BINARY = r"0[bB][01]+"
t_OCTAL = r"0[0-7]+"
t_HEX = r"0[xX][0-9A-F]+"
t_STRING = r"(?!TR\b|tr\b|FL\b|fl\b|NULL\b|null\b)[_a-zA-Z][_a-zA-Z0-9]*\b"
t_QUOTED_STRING = r'"([^"\n]*)?"'
t_TRUE = r"TR|tr"
t_FALSE = r"FL|fl"
t_NULL = r"NULL|null"


# Ignorar espacios y tabulaciones
t_ignore = " \t"


# Regla para manejar el error léxico
def t_error(t):
    print(f'Error léxico: Carácter no reconocido "{t.value[0]}"')
    t.lexer.skip(1)


# Construcción del analizador léxico
lexer = lex.lex()

# Test del analizador léxico
data = '10 420 -12 -999 0.1289 .12 -100.001 12. 10e-1 10.1E10 1.E10 5E2 .1.1E10  E54 4e-2 0b101 0B110110 B0 0b 0b010 0712 0332 01121 \
0xA0F 0X0AF _a0 a_0 Aa 0_a "hola" "" TR FL tr fl TREX trex flex "TR EX" null NULL nulla '


lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
