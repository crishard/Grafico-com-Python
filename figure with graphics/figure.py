import matplotlib.pyplot as plt

#informações para o gráfico um da figura
name = ['José', 'Francisco', 'Maria', 'Janice', 'Florinda']
age = [32, 25, 34, 16, 22]

#informações pro gráfico dois da figura
brand = ['Ferrrari', 'Audi', 'Chevrolet', 'Volkswagen']
sales = [9, 14, 11, 8]

#informações pro gráfico três da figura
product = ['Sugar', 'Coffee', 'Rice', 'Noodle']
cost = [3.43, 2.22, 4.15, 1.75]

#informações para o gráfico quatro da figura
people = ['Roberta', 'Juarez', 'Geogirna', 'Marinalva', 'Pablo']
bmi = [23.5, 32.2, 18.37, 19.14, 22.64]

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