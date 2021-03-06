# Regra de Cramer -> Determinantes
"""

A regra de Cramer tem como objetivo encontrar um métoodo
Para facilitar a busca dos valores de um sistema linear que possuem o 
mesmo número de equações e incógnitas.

"""

#Base case
"""
x + y = 10
2x + y = 15

[[1, 1],   # Coeficientes das incógnitas
 [2, 1]]

[[10],  # Termos idependentes
 [15]]

x = Dx/D , y = Dy/D ...  
"""

m2x2 = [[2,4], 
        [1,3]]

m3x3 = [[2,4,6],
        [1,2,3],
        [1,2,3]]

