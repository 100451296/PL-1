from ajson_lexer import tokens
import ply.yacc as yacc


# Reglas de la gramática
def p_object(p):
    '''object : OPEN_BRACE pairs CLOSE_BRACE'''
    p[0] = p[2]

def p_pairs(p):
    '''pairs : pair COMMA pairs
             | pair'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_pair(p):
    '''pair : key COLON value'''
    p[0] = (p[1], p[3])

def p_key(p):
    '''key : QUOTED_STRING
           | STRING'''
    p[0] = p[1]

def p_value(p):
    '''value : QUOTED_STRING
             | STRING
             | INTEGER
             | FLOAT
             | HEX
             | NULL
             | object'''
    p[0] = p[1]

    
def p_error(p):
    print("Error de sintaxis en la entrada! ", p)

# Construcción del analizador sintáctico
parser = yacc.yacc()

# Archivo de ejemplo AJSON
ajson_data = '''
{
    "this is": "AJSON",
    keys_sometimes_dont_need_quotes: "values always do",
    "you can nest other AJSON": {
        _and_have_other_types_like: 10000,
        or: 12.123,
        "another": 33,
        yet_another: NULL
    }
}
'''

# Parsear el archivo AJSON
parsed_data = parser.parse(ajson_data)
print(parsed_data)