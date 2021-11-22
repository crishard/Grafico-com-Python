import matplotlib.pyplot as plt

#informações para o gráfico um da figura
name = ['José', 'Francisco', 'Maria']
age = [32, 25, 34]

#informações pro gráfico dois da figura
brand = ['Ferrrari', 'Audi', 'Chevrolet']
sales = [9, 14, 11]

#informações pro gráfico três da figura
product = ['Sugar', 'Coffee', 'Rice']
cost = [3.43, 2.22, 4.15]

#informações para o gráfico quatro da figura
people = ['Roberta', 'Juarez', 'Geogirna']
bmi = [23.5, 32.2, 18.37]

plt.figure()

plt.subplot(221)
plt.bar(name, age)

plt.subplot(222)
plt.scatter(brand, sales)

plt.subplot(223)
plt.plot(product, cost, 'ro')

plt.subplot(224)
plt.plot(people, bmi)

plt.savefig('figure.jpeg')
plt.show()