import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from frecspace import Frecspace
from timespace import Timespace
from calculate_H import draw_H, normalize_H

R1 = 3.3E3
R3 = 1.5E3
C1 = 18E-9
C3 = 39E-9

# Calculo H según los valores provistos
num = np.array([C1**2*R1**2*C3*R3, 2*C1**2*R3*R1, 2*C1*R3, 1])
den = np.array([C1**2*R1**2*C3*R3, 2*C1**2*R1*R3 + R1**2*C1*C3 + 2*R1*C1*R3*C3, R1*C3 + 2*C1*R3 + 2*R1*C1, 1])
f0 = (den[0]/den[-1]) ** (-1 / (len(den)-1)) / (2 * np.pi)

# draw_H(num, den)        # Dibuja la H obtenida
# num2, den2 = normalize_H(num, den)  # Normaliza H
# draw_H(num2, den2)      # Dibuja nueva H

#GRÁFICOS
FS = Frecspace()        # Crea espacio de curvas de frecuencia
FS.change_title("Filtro Notch")
# Si tarda es porque el Montecarlo tiene muchos puntos
FS.add_curve(4, "Notch300.txt", "Simulación de Montecarlo", "silver", "Hz")     # Montecarlo siempre primero así queda al fondo
FS.add_curve(1, [num, den, [10E2, 10E5, 10000]], "Teórica", "blue")
FS.add_curve(2, "Notch.txt", "Simulada", "orange", "Hz")
FS.add_curve(3, "TC_TP1_Notch.csv", "Mediciones", "green")
# fig, ax = plt.subplots(1)         # Descomentar para ver sólo módulo o fase
fig, ax = plt.subplots(2, 1)        # Comentar para sólo módulo o fase
ax, ax2 = ax                        # Comentar para sólo módulo o fase
# ax2 = ax                          # Descomentar para sólo fase
fig.suptitle(FS.title)
FS.plot_mod(ax)                     # Comentar para sólo fase
FS.plot_ph(ax2)                     # Comentar para sólo módulo
fig.tight_layout()
plt.savefig(FS.title + ".jpg", dpi=300)
plt.show()


