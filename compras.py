# -*- coding: utf-8 -*-
"""Compras.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14XJHRZA_hRrQtP-AcOTnosG0qmA2ENeH
"""

frutas = ['maça', 'banana', 'pera','uva' ]
guloseimas = ['bolacha','batata', 'fini', 'chocolate' ]
comida = ['arroz','feijão', 'carne' ]
bebidas = ['refrigerante','suco de laranja', 'água' ]

categorias =  ['fruta','guloseimas', 'comida', 'bebidas' ]
compras = [frutas, guloseimas, comida, bebidas ]

for indice, categoria in enumerate(categorias):
  print('você precisa comprar', len(compras[indice]), categoria +':')
  for compra in compras[indice]:
    print('-', compra)

