A = int(input('digite um numero'))
conta = input('digite o símbolo para realizar a operação')
B = int(input('digite o segundo numero'))
if conta == '+':
  print(A + B)
elif conta == '-':
  print(A - B)
elif conta == '/':
  print(A / B)
elif conta == '*':
  print(A * B)
elif conta == '**':
  print(A**B)
else:
  print('Digite uma operação válida')