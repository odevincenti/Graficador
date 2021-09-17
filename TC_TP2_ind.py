import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from frecspace import Frecspace
from timespace import Timespace
from calculate_H import draw_H, normalize_H

R1 = 1E3
R2 = 10E3
R3 = 1E3
R4 = 22E3
Ao = 100E3
fb = 40
wb = 2*np.pi*fb
interval = [1, 2E6, 1E4]

GI = -R2/R1
f0 = (Ao * fb)/(1 + R2 * (R1 + R3)/(R1 * R3))

def G(s, unit="rad/s"):
    w0 = 2 * np.pi * f0
    if unit != "Hz":
        s = 2 * np.pi * s
    Gs = GI/(1 + 1j * s/w0)
    Gmod = np.abs(Gs)
    Gph = np.angle(Gs, deg=True)
    return Gmod, Gph

# Calculo H según los valores provistos
w0 = 2 * np.pi * f0
num = GI * np.array([1])
den = np.array([1/w0, 1])

#GRÁFICOS
FS = Frecspace()        # Crea espacio de curvas de tiempo
FS.change_title("Ganancia del circuito inversor")


FS.add_curve(1, [num, den, [1, 2E6, 1E5]], "Caso 1")
R2 = 15E3
GI = -R2/R1
f0 = (Ao * fb)/(1 + R2 * (R1 + R3)/(R1 * R3))
w0 = 2 * np.pi * f0
num = GI * np.array([1])
den = np.array([1/w0, 1])

FS.add_curve(1, [num, den, [1, 2E6, 1E5]], "Caso 2")

R2 = 22E3
GI = -R2/R1
f0 = (Ao * fb)/(1 + R2 * (R1 + R3)/(R1 * R3))
w0 = 2 * np.pi * f0
num = GI * np.array([1])
den = np.array([1/w0, 1])

FS.add_curve(1, [num, den, [1, 2E6, 1E5]], "Caso 3")


# Si tarda es porque el Montecarlo tiene muchos puntos
'''
FS.add_curve(4, "D:\Documentos\Materias\\22.01 - TC\TP2 Individual\Simulaciones\Inversor\Inv_mc10k_Vo.txt", "Montecarlo", "silver", "Hz")
FS.add_curve(1, [num, den, [1, 2E6, 1E5]], "Teórica", "blue")
FS.add_curve(2, "D:\Documentos\Materias\\22.01 - TC\TP2 Individual\Simulaciones\Inversor\Inv10k_Vo.txt", "Simulación", "orange", "Hz")
FS.add_curve(3, "D:\Documentos\Materias\\22.01 - TC\TP2 Individual\Bode_10k.csv", "Medicion", "green", "Hz")'''

FS.set_interval([1E3, 2E6])
fig, ax = plt.subplots(1)         # Descomentar para ver sólo módulo o fase
#fig, ax = plt.subplots(2, 1)        # Comentar para sólo módulo o fase
#ax, ax2 = ax                        # Comentar para sólo módulo o fase
# ax2 = ax                          # Descomentar para sólo fase
fig.suptitle(FS.title)
FS.plot_mod(ax)
#FS.plot_ph(ax2)
fig.tight_layout()
# plt.savefig(TS.title + ".jpg", dpi=300)
plt.show()

