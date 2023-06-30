import datetime
dia_de_nascimento = int(input('insira sua data de nascimento:'))
mês_de_nascimento = int(input('insira seu mês de nascimento:'))
ano_de_nascimento = int(input('insira seu ano de nascimento:'))

print(f'Pelos dados escritos você tem {datetime.date.today().year - ano_de_nascimento} anos, {datetime.date.today().month - mês_de_nascimento} meses e {int(str(datetime.date.today().day)) - dia_de_nascimento} dias.')