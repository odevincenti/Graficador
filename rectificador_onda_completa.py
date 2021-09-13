import matplotlib.pyplot as plt
import numpy as np

# Salida teórica del rectificador de onda completa
n = 2       # Cantidad de curvas
titulo = "Rectificador de onda completa"
xlabel = "tiempo"
ylabel = "Tensión"
x0 = 0
xf = 6*np.pi
puntos = 1000
A = 4.0
V_D_ON = 0.7
xlim = [x0, xf]
ylim = [-A - 2*V_D_ON, A + 2*V_D_ON]
xticks = [0, np.pi, 2*np.pi, 3*np.pi, 4*np.pi, 5*np.pi, 6*np.pi]
xticklabels = ["$0$", "", "$T$", "", "$2T$", "", "$3T$"]
yticks = [-A, -A + 2*V_D_ON, -(A - 2*V_D_ON)/2, 0, (A - 2*V_D_ON)/2, A - 2*V_D_ON, A]
yticklabels = ["$-A$", "", "", "$0$", "", "$A - 2V_D$", "A"]

def fun(Vi):
    Vo = [0.0] * len(Vi)
    for i in range(len(Vi)):
        if - 2 * V_D_ON < Vi[i] < 2 * V_D_ON:
            Vo[i] = 0.0
        else:
            Vo[i] = np.abs(Vi[i]) - 2*V_D_ON
    return Vo

x = np.linspace(x0, xf, puntos)
y = [None] * n
label = [""] * n
color = [""] * n
y[0] = A*np.sin(x)
label[0] = "Entrada"
color[0] = "gold"
y[1] = fun(y[0])
label[1] = "Salida"
color[1] = "mediumblue"

fig, ax = plt.subplots(1)
for i in range(len(y)):
    ax.plot(x, y[i], label=label[i], color=color[i])
ax.set_title(titulo)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels)
ax.set_yticks(yticks)
ax.set_yticklabels(yticklabels)
ax.legend()
ax.grid()
fig.tight_layout()
plt.show()
