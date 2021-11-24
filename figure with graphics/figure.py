import matplotlib.pyplot as plt

#informações para o gráfico um da figura
name = ['José', 'Francisco', 'Maria']
age = [32, 25, 34]
#título do gráfico um e nomeando os eixos
plt.title('Gráfico de barras')
plt.xlabel('Eixo x')
plt.ylabel('Eixo Y')

#informações pro gráfico dois da figura
brand = ['Ferrrari', 'Audi', 'Chevrolet']
sales = [9, 14, 11]
#título do gráfico dois e nomeando os eixos
plt.title('Gráfico de pontos')
plt.xlabel('Eixo x')
plt.ylabel('Eixo Y')

#informações pro gráfico três da figura
product = ['Sugar', 'Coffee', 'Rice']
cost = [3.43, 2.22, 4.15]
#título do gráfico três e nomeando os eixos
plt.title('Gráfico de pontos vermelhos')
plt.xlabel('Eixo x')
plt.ylabel('Eixo Y')

#informações para o gráfico quatro da figura
people = ['Roberta', 'Juarez', 'Geogirna']
bmi = [23.5, 32.2, 18.37]
#título do gráfico quatro e nomeando os eixos
plt.title('Gráfico de linhas')
plt.xlabel('Eixo x')
plt.ylabel('Eixo Y')

#criando gráfico um
plt.subplot(221)
plt.bar(name, age)

#criando gráfico dois
plt.subplot(222)
plt.scatter(brand, sales)

#criando gráfico três
plt.subplot(223)
plt.plot(product, cost, 'ro')

#criando gráfico quatro
plt.subplot(224)
plt.plot(people, bmi)

#dando título a figura
plt.suptitle('Titulo da figura')
#salvando a figuta como imagem
plt.savefig('figure.jpeg')
#mostrando a figura
plt.show()