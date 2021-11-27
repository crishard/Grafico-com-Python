import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects

#criando o texto, escolhendo a posição que ele vai ter no gráfico e adicionando um efeito a ele 
text = plt.text(1.5, 1.5, 'Hello effects!',
                path_effects=[path_effects.withSimplePatchShadow()])

#criando o gráfico, com o máximo do eixo y, sua cor e efeito
plt.plot([1, 5, 3, 7], linewidth=10, color='green',
         path_effects=[path_effects.SimpleLineShadow(),
                       path_effects.Normal()])
#título
plt.title('Path effects')

#salvando e mostrando a imagem
plt.savefig('path_effects,jpeg')
plt.show()