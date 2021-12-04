import matplotlib.pyplot as plt

figure, aux = plt.subplots()

circle = plt.Circle((0, 0), 0.6, color='white')
lbs = ['Dormir', 'Ler', 'Estudar', 'Comer']

aux.pie([6, 3, 8, 9],
labels=lbs, autopct= '%1.1f%%',
pctdistance=0.82)

aux.add_artist(circle)
aux.set_title('Circle chart', fontsize=18)

plt.savefig('cicle.jpg')

plt.show()