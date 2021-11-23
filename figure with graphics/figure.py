import matplotlib.pyplot as plt

#informações para o gráfico um da figura
name = ['José', 'Francisco', 'Maria']
age = [32, 25, 34]
plt.title('Gráfico de barras')
plt.xlabel('Eixo x')
plt.ylabel('Eixo Y')

#informações pro gráfico dois da figura
brand = ['Ferrrari', 'Audi', 'Chevrolet']
sales = [9, 14, 11]
plt.title('Gráfico de pontos')
plt.xlabel('Eixo x')
plt.ylabel('Eixo Y')

#informações pro gráfico três da figura
product = ['Sugar', 'Coffee', 'Rice']
cost = [3.43, 2.22, 4.15]
plt.title('Gráfico de pontos vermelhos')
plt.xlabel('Eixo x')
plt.ylabel('Eixo Y')

#informações para o gráfico quatro da figura
people = ['Roberta', 'Juarez', 'Geogirna']
bmi = [23.5, 32.2, 18.37]
plt.title('Gráfico de linhas')
plt.xlabel('Eixo x')
plt.ylabel('Eixo Y')

plt.subplot(221)
plt.bar(name, age)

plt.subplot(222)
plt.scatter(brand, sales)

plt.subplot(223)
plt.plot(product, cost, 'ro')

plt.subplot(224)
plt.plot(people, bmi)

plt.suptitle('Titulo da figura')
plt.savefig('figure.jpeg')
plt.show()