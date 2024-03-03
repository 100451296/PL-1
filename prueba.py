import ply.lex as lex
import ply.yacc as yacc

# Definición de tokens
tokens = (
    "NUMBER",
    "PLUS",
    "MINUS",
)


# Reglas de expresiones regulares para tokens
t_PLUS = r"\+"
t_MINUS = r"-"


# Definición de la función para el token NUMBER
def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    print("TOKEN:", t.value)
    return t


# Ignorar espacios y tabulaciones
t_ignore = " \t"


# Manejo de errores (siempre hay que ponerla)
def t_error(t):
    print("Error léxico: Carácter no reconocido '%s'" % t.value[0])
    t.lexer.skip(1)


# Construcción del analizador léxico
lexer = lex.lex()


# Definición de la gramática
def p_expression_plus(p):
    "expression : expression PLUS expression"
    for token in p:
        print("PLUS", token, end=" | ")
    print()
    p[0] = p[1] + p[3]


def p_expression_minus(p):
    "expression : expression MINUS expression"

    for token in p:
        print("MINUS:", token, end=" | ")
    print()
    p[0] = p[1] - p[3]


def p_expression_number(p):
    "expression : NUMBER"
    p[0] = p[1]


def p_error(p):
    print("Error sintáctico: Sintaxis incorrecta en '%s'" % p.value)


# Construcción del analizador sintáctico
parser = yacc.yacc(debug=True)

# Ejemplo de uso
data = "1 + 1 + 2"
result = parser.parse(data)
print("Resultado:", result)
