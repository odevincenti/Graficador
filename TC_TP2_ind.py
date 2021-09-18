import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from frecspace import Frecspace
from timespace import Timespace
from calculate_H import draw_H, normalize_H

def G(s, unit="rad/s"):
    w0 = 2 * np.pi * fo
    if unit != "Hz":
        s = 2 * np.pi * s
    Gs = GI/(1 + 1j * s/w0)
    Gmod = np.abs(Gs)
    Gph = np.angle(Gs, deg=True)
    return Gmod, Gph

def par(Ra, Rb):
    Req = 1/(1/Ra + 1/Rb)
    return Req

R1 = 1E3
R2 = 22E3
R3 = 1E3
R4 = 22E3
Ao = 200E3
fb = 15
wb = 2*np.pi*fb
interval = [1, 2E6, 1E4]

GI = -R2/R1
fo = (Ao * fb)/(1 + R2 * (R1 + R3)/(R1 * R3))

# CALCULO GANANCIA
wo = 2 * np.pi * fo
num = GI * np.array([1])
den = np.array([1/wo, 1])

# CALCULO IMPEDANCIA DE ENTRADA
fn = Ao * fb / (R2/par(R1, R3))
wn = 2 * np.pi * fn
fd = Ao * R3 * fb / R2
wd = 2 * np.pi * fd
numZi = [-R1/wn, -R1]
denZi = [1/wd, 1]

print("R2 = ", R2)
print("fo = ", fo)
print("fn ", fn)
print("wn = ", wn)
print("fd ", fd)
print("wd = ", wd)

#GRÁFICOS
FS = Frecspace()        # Crea espacio de curvas de tiempo

'''
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
'''

# Si tarda es porque el Montecarlo tiene muchos puntos

param = "Zi"
# FS.change_title("Ganancia del circuito inversor - Caso " + str(int(round((-1*(R2/1E3)**2 + 67 * R2/1E3 - 360)/210))))
FS.change_title("Impedancia de entrada circuito inversor")

FS.add_curve(4, "D:\Documentos\Materias\\22.01 - TC\TP2 Individual\Simulaciones\Inversor\Inv_mc" + str(int(round(R2/1E3))) + "k_" + param + ".txt", "Montecarlo", "silver", "Hz")
FS.add_curve(1, [numZi, denZi, [1, 2E6, 1E5]], "Teórica", "blue")
FS.add_curve(2, "D:\Documentos\Materias\\22.01 - TC\TP2 Individual\Simulaciones\Inversor\Inv" + str(int(round(R2/1E3))) + "k_" + param + ".txt", "Simulación", "orange", "Hz")
FS.add_curve(3, "D:\Documentos\Materias\\22.01 - TC\TP2 Individual\Mediciones\Inv" + str(int(round(R2/1E3))) + "k_" + param + ".csv", "Medicion", "green", "Hz", "veces")
# FS.change_mod_unit("veces")
# FS.change_ph_unit("rad")
#FS.change_y_mod_label("$Z_{inp}[Ohm]$")
#FS.change_y_ph_label("$\\angle Z_{inp}$")

FS.set_interval([1E3, 2E6])
#fig, ax = plt.subplots(1)         # Descomentar para ver sólo módulo o fase
fig, ax = plt.subplots(2, 1)        # Comentar para sólo módulo o fase
ax, ax2 = ax                        # Comentar para sólo módulo o fase
# ax2 = ax                          # Descomentar para sólo fase
fig.suptitle(FS.title)
FS.plot_mod(ax)
FS.plot_ph(ax2)
fig.tight_layout()
# plt.savefig(TS.title + ".jpg", dpi=300)
plt.show()

