from ajson_lexer import scanner
from ajson_parser import parser, EMPTY
import sys

# Código de colores ANSI
GREEN = "\033[92m"
RESET = "\033[0m"


def print_formatted(key, value, prefix=""):
    if isinstance(value, list):
        for i, v in enumerate(value):
            if isinstance(v, tuple):
                print_formatted(f"{key}.{v[0]}", v[1], prefix)
            elif isinstance(v, list):
                print_formatted(f"{key}.{i}", v, prefix)
    else:
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

if parsed_data == EMPTY:
    print(">> FICHERO AJSON VACIO", GREEN + input_file + RESET)
elif parsed_data:
    print(">> FICHERO AJSON", GREEN + input_file + RESET)
    for pair in parsed_data:
        print_formatted(pair[0], pair[1])
