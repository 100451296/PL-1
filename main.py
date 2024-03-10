from ajson_lexer import scanner
from ajson_parser import parser, EMPTY
import sys

# Código de colores ANSI
GREEN = "\033[92m"
RESET = "\033[0m"


def print_formatted(key, value, prefix=""):
    """
    Imprime las tuplas clave:valor, se llama de manera de recursiva dado que la profundidad del AJSON no es conocida.
    En caso de detectar dos listas anidadas consecutivamente, se ha encontrado un array, por lo que añade el indice
    del objeto como parte de la clave.
    """
    if isinstance(value, list):
        for i, v in enumerate(value):
            # Objeto
            if isinstance(v, tuple):
                print_formatted(f"{key}.{v[0]}", v[1], prefix)
            # Lista detectada
            elif isinstance(v, list):
                print_formatted(f"{key}.{i}", v, prefix)
    else:
        # Caso base (objeto)
        print("{ ", f"{prefix}{key}: {value}", " }")


data = str()

# Tratamiento de argumentos
if len(sys.argv) < 2:
    print(f"Uso: python main.py input_file")
    sys.exit(0)
input_file = sys.argv[1]

# Lectura de archivo de entrada
try:
    # Abrir el archivo y leer su contenido
    with open(input_file, "r") as file:
        data = file.read()
except FileNotFoundError:
    print(f"El archivo {input_file} no pudo ser encontrado.")
    sys.exit(0)

# Ejecucion del analizador
parsed_data = parser.parse(data)

# Caso AJSON vacio
if parsed_data == EMPTY:
    print(">> FICHERO AJSON VACIO", input_file)
# Imprime las tuplas
elif parsed_data:
    print(">> FICHERO AJSON", input_file)
    for pair in parsed_data:
        print_formatted(pair[0], pair[1])
