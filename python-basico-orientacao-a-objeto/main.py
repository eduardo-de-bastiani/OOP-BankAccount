from veiculos import Veiculo
from carros import Carro

caminhao_rosa = Veiculo('rosa', 6, 'Ford', 80)
print ('CAMINHAO ROSA')
print ('Cor: ', caminhao_rosa.cor)
print ('Rodas: ', caminhao_rosa.rodas)
print ('Marca: ', caminhao_rosa.marca)
print ('Tanque: ', caminhao_rosa.tanque)

print ('')

carro_azul = Carro('azul', 'BMW', 30)                       # Não precisa mais passar o numero de rodas, pq já foi especificado na class Carro
print ('CARRO AZUL')
print ('Cor: ', carro_azul.cor)
print ('Rodas: ', carro_azul.rodas)
print ('Marca: ', carro_azul.marca)
print ('Tanque: ', carro_azul.tanque)
carro_azul.abastecer(10)
print ('Novo Tanque: ', carro_azul.tanque)
carro_azul.abastecer(18)
print ('Novo tanque: ', carro_azul.tanque)


