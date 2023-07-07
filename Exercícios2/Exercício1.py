velocidade = float(input('insira a velocidade em Km/h:'))

if velocidade > 80:
  print('Seu veículo foi multado.')
  print(f'Devido sua velocidade excessiva você vai ter que pagar R${(velocidade - 80) * 7} de multa.')
else:
  print('Tudo de boa com sua velocidade.')