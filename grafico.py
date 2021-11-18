import matplotlib.pyplot as grf

grf.title('Faturaamento em 2021')
grf.xlabel('Meses')
grf.ylabel('Faturamento em R$')
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

valores = [520, 245, 322, 587, 360, 142, 189, 680, 470, 155, 169, 520]

""""grf.scatter para grafico de pontos
    grf.plot para grafico de linhas"""
grf.bar(meses, valores)
grf.show()

