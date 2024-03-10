#!/bin/bash

# Definir colores
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

# Imprimir mensaje de prueba con color
printf "${GREEN}### TESTs ###${NC}"
echo -e "\n"

# Iterar sobre cada archivo .ajson en la carpeta test_files
for file in test_files/*.ajson; do
    echo -e "${YELLOW}Testing $file ...${NC}"
    # Ejecutar el comando python3 main.py para cada archivo
    python3 main.py "$file"
    echo -e "\n"
done
