from modelos.restaurantes import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca=Restaurante('Praça','Gourmet')
restaurante_mexicano=Restaurante('Mexican Food','Mexicana')
restaurante_japones=Restaurante('Japa','Japonesa')
bebida_suco=Bebida('Suco de melancia',5.00,'Grande')
prato_paozinho=Prato('Pãozinho',2.00,'O melhor pãozinho da cidade')
restaurante_praca.adicionar_bebida_no_cardapio(bebida_suco)
restaurante_praca.adicionar_prato_no_cardapio(prato_paozinho)

def main():
    pass


if __name__=='__main__':
    main()