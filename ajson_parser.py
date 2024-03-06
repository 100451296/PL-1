from ajson_lexer import tokens
import ply.yacc as yacc

EMPTY = "vacio"


# Reglas de la gramática
def p_object(p):
    """object : OPEN_BRACE pairs CLOSE_BRACE
    | OPEN_BRACE CLOSE_BRACE"""
    p[0] = p[2] if p[2] != "}" else EMPTY


def p_array(p):
    """array : OPEN_BRACKET objects CLOSE_BRACKET"""
    p[0] = p[2]


def p_objects(p):
    """objects : object COMMA object 
    | object"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]


def p_pairs(p):
    """pairs : pair COMMA pairs
    | pair"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]


def p_pair(p):
    """pair : key COLON value
    | key COLON comparation
    | key COLON array"""
    p[0] = (p[1], p[3])


def p_key(p):
    """key : QUOTED_STRING
    | STRING"""
    p[0] = p[1]


def p_comparation(p):
    """comparation : number comp number"""
    if p[2] == "==":
        p[0] = p[1] == p[3]
    elif p[2] == ">":
        p[0] = p[1] > p[3]
    elif p[2] == ">=":
        p[0] = p[1] >= p[3]
    elif p[2] == "<":
        p[0] = p[1] < p[3]
    elif p[2] == "<=":
        p[0] = p[1] <= p[3]
    else:
        p[0] = None  # Caso error, nunca deberia llegar a aqui (error lexico)


def p_number(p):
    """number : INTEGER
    | FLOAT
    | HEX
    | SCIENTIFIC
    | OCTAL
    | BINARY
    """
    p[0] = p[1]


def p_comp(p):
    """comp : EQUAL
    | GRATER_EQUAL
    | LOWER_EQUAL
    | GRATER
    | LOWER
    """
    p[0] = p[1]


def p_value(p):
    """value : QUOTED_STRING
    | INTEGER
    | FLOAT
    | HEX
    | SCIENTIFIC
    | OCTAL
    | BINARY
    | NULL
    | TRUE
    | FALSE
    | object"""
    p[0] = p[1]


def p_error(p):
    print("Error de sintaxis en la entrada! ", p)


# Construcción del analizador sintáctico
parser = yacc.yacc()

if __name__ == "__main__":

    # Archivo de ejemplo AJSON
    ajson_data = """
  {
      "this is": "AJSON",
      keys_sometimes_dont_need_quotes: "values always do",
      "integer": 123,
      "float": 3.14,
      "hexadecimal": 0xABC,
      "scientific": 1.23e10,
      "octal": 0123,
      "binary": 0b1010,
      "null": null,
      "true": tr,
      "false": fl,
      "nested_object": {
          "key1": "value1",
          "key2": 42
      },
      "equal": 1e-1 == 0.1,
      "grater": 5 > 3,
      "grater_equal": 0xFF >= 0b111011,
      "lower": 077 < 64,
      "lower_equal": 273 <= 0b1011011100000000
  }
  """

    # Parsear el archivo AJSON
    parsed_data = parser.parse(ajson_data)
    print(parsed_data)
