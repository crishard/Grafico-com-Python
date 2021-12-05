import matplotlib.pyplot as plt

#criando figura
figure, aux = plt.subplots()

#criando o circulo e as informações que farão parte dele
circle = plt.Circle((0, 0), 0.6, color='white')
lbs = ['Dormir', 'Ler', 'Estudar', 'Comer']

#criando o gráfico, alocando as informações em porcentagem
aux.pie([6, 3, 8, 9],
labels=lbs, autopct= '%1.1f%%',
pctdistance=0.82)

#adicionando o circulo a figura
aux.add_artist(circle)
aux.set_title('Circle chart', fontsize=18)

#salvando e mostrando a figura
plt.savefig('cicle.jpg')
plt.show()