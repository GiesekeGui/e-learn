km_rodados = float(input('insira a quantidade de km rodados:'))
dias = int(input('insira a quantidade de dias alugados:'))

print(f'Se você alugou por {dias} dias e dirigiu {km_rodados} Km\nO total a pagar é de R${(km_rodados * 0.15) + (dias * 60)}.')