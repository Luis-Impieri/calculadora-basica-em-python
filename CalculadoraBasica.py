import math

A = float(input('digite um numero'))
conta = input('digite o símbolo para realizar a operação')
B = float(input('digite o segundo numero'))
if conta == '+':
  print(A + B)
elif conta == '-':
  print(A - B)
elif conta == '/':
  if B == 0:
    print('Não é possível dividir po Zero')
  else:
    print(A / B)
elif conta == '*':
  if B == 0:
    print('Não é possível multiplicar por Zero')
  else:
    print(A * B)
elif conta == '**':
  print(A**B)

elif conta == "//":
  print(math.sqrt(A))

elif conta == "log":
  print(math.log(A, B))

elif conta == "$":
  print("sen ",math.sin(A), "cos ",math.cos(A), "tan ",math.tan(A))

else:
  print('Digite uma operação válida')