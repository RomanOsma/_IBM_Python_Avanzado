import re

texto = "El código es 987-654"
patron = re.compile(r"(\d+)-(\d+)")

match = patron.search(texto)

if match:
    print("Grupo completo:", match.group())     # 987-654
    print("Grupo 1:", match.group(1))           # 987
    print("Grupo 2:", match.group(2))           # 654
    print("Start grupo 1:", match.start(1))     # índice
    print("End grupo 2:", match.end(2))         # índice
    print("Span total:", match.span())          # (13, 20)
    print("Texto original:", match.string)      # El código es 987-654
