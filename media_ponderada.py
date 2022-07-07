# Media Ponderada

"""
n = Quantidade de notas
grades = [nota1, nota2, ...]
grades = [peso_nota1, peso_nota2, ...]
"""

def media(n, grades=[],pesos=[]):
    """Cálculo da Média Ponderada"""
    calc = sum([grades[i]*pesos[i] for i in range(n)])/sum(pesos)
    return calc

n = 3 
grades = [78,90,100]
pesos = [3,5,2]

print(media(n, grades, pesos))