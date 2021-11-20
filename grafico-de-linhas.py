#importando biblioteca e colocando o comando "grf" como comando da bibioteca
import matplotlib.pyplot as grf

#definindo título para o gráfico
grf.title('Faturamento em 2021')

#informações que serão exibidaas no eixo x
grf.xlabel('Meses')

#informações que serão exibidas no eixo y
grf.ylabel('Faturamento em R$')

#criando as listas de dados
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

valores = [520, 245, 322, 587, 360, 142, 189, 680, 470, 155, 169, 520]

#utilizando gráfico de linhas
grf.plot(meses, valores)

#chamando função para apresentar o gráfico
grf.show()

