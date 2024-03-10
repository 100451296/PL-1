#!/bin/bash

# Definir colores
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

# Verificar el sistema operativo
if [[ "$OSTYPE" == "msys" ]]; then
    # Si se está ejecutando en Windows (MSYS), usar python en lugar de python3
    PYTHON_CMD="python"
else
    # Si no es Windows, utilizar python3
    PYTHON_CMD="python3"
fi

# Imprimir mensaje de prueba con color
printf "${GREEN}### TESTs ###${NC}"
echo -e "\n"

# Iterar sobre cada archivo .ajson en la carpeta test_files
for file in test_files/*.ajson; do
    echo -e "${YELLOW}Testing $file ...${NC}"
    # Ejecutar el comando python (o python3) main.py para cada archivo
    "$PYTHON_CMD" main.py "$file"
    echo -e "\n"
done

read
