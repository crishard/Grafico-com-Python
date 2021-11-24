#importando biblioteca e colocando o comando "grf" como comando da bibioteca
import matplotlib.pyplot as grf

#definindo título para o gráfico
grf.title('Vendas em outubro de 2021')

#informações que serão exibidaas no eixo x
grf.xlabel('Dias')

#informações que serão exibidas no eixo y
grf.ylabel('Faturamento em R$')

#criando as listas de dados
dias = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]


valores = [520, 245, 322, 587, 360, 142, 189, 680, 470, 155, 169, 520, 369, 145, 258, 265, 145, 198, 169, 201, 596, 148, 256, 248, 279, 364, 157, 248, 352, 450, 489 ]

#utilizando gráfico de pontos
grf.scatter(dias, valores)

#chamando função para apresentar o gráfico
grf.show()

