import matplotlib.pyplot as plt
import numpy as np

# GRÁFICO TEÓRICO GENÉRICO
n = 2       # Cantidad de curvas
titulo = "Title"
xlabel = "Eje x"
ylabel = "Eje y"
x0 = 0
xf = 10
puntos = 1000
A = 1.0
xlim = [x0, xf]
ylim = [-A*1.25, A*1.25]
ticks = False       # Poner en True para customizar los labels
if ticks:
    xticks = [x0, 0.2*(xf-x0) + x0, 0.4*(xf-x0) + x0, 0.6*(xf-x0) + x0, 0.8*(xf-x0) + x0, xf]
    xticklabels = ["$x_o$", "", "", "", "", "$x_f$"]
    yticks = [-A, -A*0.75, -A*0.5, -A*0.25, 0, A*0.25, A*0.5, A*0.75, A]
    yticklabels = ["$-A$", "", "", "", "$0$", "", "", "", "A"]

def fun(Vi):
    Vo = np.abs(Vi)
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
if ticks:
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels)
    ax.set_yticks(yticks)
    ax.set_yticklabels(yticklabels)
ax.legend()
ax.grid()
fig.tight_layout()
plt.show()







