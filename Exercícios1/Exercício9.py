try:
   dado1 = type(int(input('insira o primeiro dado:')))
except:
   dado1 = str
try:
   dado2 = type(int(input('insira o segundo dado:')))
except:
   dado2 = str
print(f'tipo dado1: {dado1}')
print(f'tipo dado2: {dado2}')
print({dado1} == {dado2})