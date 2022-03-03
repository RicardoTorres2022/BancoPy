from models.cliente import Cliente
from models.conta import Conta

duque: Cliente = Cliente('Duque de Gorgonzola', '10.201.301', '013.210.333-55', '20/05/2012', 'duque@gmail.com')
bartholomeu: Cliente = Cliente('Bartholomeu Feio', '20.301.456', '456.789.001-20', '15/03/2017', 'bart@gmail.com')

print(duque)
#print(bartholomeu)

contaf: Conta = Conta(duque)

print(contaf)
