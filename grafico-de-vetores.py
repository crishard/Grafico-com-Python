import matplotlib.pyplot as plt

a = [0, 5, 10, 15, 20, 25, 35, 40]
b = [0, 15, 20, 30, 35]
z = [0, 10, 20, 30, 40]

figure, geral = plt.subplots()

geral.plot(a, label='var a')
geral.plot(b, label='var b')
geral.plot(z, label='var z')


plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.title('Título')

geral.legend()

plt.show()