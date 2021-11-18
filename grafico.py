#importando biblioteca e colocando o comando "grf" como comando da bibioteca
import matplotlib.pyplot as grf

#definindo título para o gráfico
grf.title('Faturaamento em 2021')

#informações eixo x
grf.xlabel('Meses')

#informações eixo y
grf.ylabel('Faturamento em R$')

#criando as listas de dados
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

valores = [520, 245, 322, 587, 360, 142, 189, 680, 470, 155, 169, 520]

#escolhendo o gráfico
""""grf.scatter para grafico de pontos
    grf.plot para grafico de linhas"""
grf.bar(meses, valores)

#chamando função para apresentar o gráfico
grf.show()

