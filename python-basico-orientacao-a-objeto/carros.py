from veiculos import Veiculo

class Carro(Veiculo):                                            # Herança de classe. Peguei o def do veiculo e irei especifica-lo na class Carro
    def __init__(self, cor, marca, tanque):                      # Tirei o argv 'rodas' e defini como 4
        Veiculo.__init__(self, cor, 4, marca, tanque)

    def abastecer(self, litros):
       if self.tanque + litros > 50:
           print ('Tanque com capacidade inferior!')
       else:
            self.tanque += litros
