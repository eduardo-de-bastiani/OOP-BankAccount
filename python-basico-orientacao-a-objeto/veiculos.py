class Veiculo:                                                      # 'class' é o projeto do objeto. É ele que irá criá-lo 
    def __init__(self, cor, rodas, marca, tanque):                          # '__init__' é o construtor do objeto
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque

    def abastecer(self, litros):
        self.tanque += litros