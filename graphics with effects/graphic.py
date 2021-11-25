import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects

text = plt.text(1.5, 1.5, 'Hello effects!',
                path_effects=[path_effects.withSimplePatchShadow()])

plt.plot([1, 5, 3, 7], linewidth=10, color='green',
         path_effects=[path_effects.SimpleLineShadow(),
                       path_effects.Normal()])

plt.savefig('path_effects,jpeg')
plt.show()