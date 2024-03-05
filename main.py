from ajson_lexer import scanner

# Test del analizador léxico
data = '10 420 -12 -999 0.1289 .12 -100.001 12. 10e-1 10.1E10 1.E10 5E2 .1.1E10  E54 4e-2 0b101 0B110110 B0 0b 0b010 0712 0332 01121 \
0xA0F 0X0AF _a0 a_0 Aa 0_a "hola" "" TR FL tr fl TREX trex flex "TR EX" null NULL nulla "1==1" 1==1 1>2 1>=2 1<2 1<=1 { } : , {hola:2==2}'

# Abrir el archivo y leer su contenido
with open('example.ajson', 'r') as file:
    data = file.read()

scanner.input(data)
while True:
    tok = scanner.token()
    if not tok:
        break
    print(tok)
