preço = 0

distância = float(input('insira a distância da viagem:'))
if distância <= 200:
 preço = distância * 0.45
else:
 preço = distância * 0.50

print(f'Pela distância (distância)Km, tem que pagar:(preço)R$.')
//Okay//