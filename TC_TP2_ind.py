import matplotlib.pyplot as plt
import numpy as np
import os
# import sympy as sp
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
R2 = 10E3
R3 = 1E3
R4 = 22E3
Ao = 200E3
fb = 15
wb = 2*np.pi*fb
interval = [1, 2E6, 1E4]
circuit = "No Inversor"
param = "Zi"
plot_fo = False
#modlim_inf = 22E3       # Límite inferior del módulo (Sí, es una atada con alambre)
#modlim_sup = 24E3       # Límite superior del módulo (Sí, es una atada con alambre)

if circuit == "Inversor":
    doc_name = "Inv"
    GI = -R2/R1
    fo = (Ao * fb)/(1 + R2 * (R1 + R3)/(R1 * R3))

    # CALCULO GANANCIA
    wo = 2 * np.pi * fo
    num = GI * np.array([1])
    den = np.array([1/wo, 1])

    # CALCULO IMPEDANCIA DE ENTRADA
    fn = Ao * fb / (1 + R2 / par(R1, R3))
    wn = 2 * np.pi * fn
    fd = Ao * R3 * fb / (R2 + R3)
    wd = 2 * np.pi * fd
    numZi = [R1/wn, R1]
    denZi = [1/wd, 1]

    print("R2 = ", R2)
    print("GI = ", GI)
    print("fo = ", fo)
    print("fn ", fn)
    print("wn = ", wn)
    print("fd ", fd)
    print("wd = ", wd)

elif circuit == "No Inversor":
    doc_name = "NoInv"
    GI = R4 * (R1 + R2)/(R1 * (R3 + R4))
    fo = (Ao * fb) * R1 / (R1 + R2)

    # CALCULO GANANCIA
    wo = 2 * np.pi * fo
    num = GI * np.array([1])
    den = np.array([1 / wo, 1])

    # CALCULO IMPEDANCIA DE ENTRADA
    Zi = R3 + R4
    numZi = [Zi]
    denZi = [1]

    print("R2 = ", R2)
    print("GI = ", GI)
    print("fo = ", fo)
    print("Zi = ", Zi)

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

if param == "G":
    FS.change_title("Ganancia del Circuito " + circuit + " - Caso " + str(int(round((-1*(R2/1E3)**2 + 67 * R2/1E3 - 360)/210))))
    mod_unit = "dB"
elif param == "Zi":
    FS.change_title("Impedancia de entrada de Circuito " + circuit + " - Caso " + str(int(round((-1*(R2/1E3)**2 + 67 * R2/1E3 - 360)/210))))
    num = numZi
    den = denZi
    FS.change_mod_unit("veces")
    FS.change_y_mod_label("$Z_{inp}[\\Omega]$")
    FS.change_y_ph_label("$\\angle Z_{inp}$")
    mod_unit = "veces"

FS.add_curve(4, "D:\Documentos\Materias\\22.01 - TC\TP2 Individual\Simulaciones\\" + circuit + "\\" + doc_name + "_mc" + str(int(round(R2/1E3))) + "k_" + param + ".txt", "Montecarlo", "silver", "Hz")
FS.add_curve(1, [num, den, [1, 2E6, 1E5]], "Teórica", "blue")
FS.add_curve(2, "D:\Documentos\Materias\\22.01 - TC\TP2 Individual\Simulaciones\\" + circuit + "\\" + doc_name + str(int(round(R2/1E3))) + "k_" + param + ".txt", "Simulación", "orange", "Hz")
FS.add_curve(3, "D:\Documentos\Materias\\22.01 - TC\TP2 Individual\Mediciones\\" + doc_name + str(int(round(R2/1E3))) + "k_" + param + ".csv", "Medicion", "green", "Hz", mod_unit)

FS.set_interval([1E3, 2E6])
#fig, ax = plt.subplots(1)         # Descomentar para ver sólo módulo o fase
fig, ax = plt.subplots(2, 1)        # Comentar para sólo módulo o fase
ax, ax2 = ax                        # Comentar para sólo módulo o fase
# ax2 = ax                          # Descomentar para sólo fase
fig.suptitle(FS.title)
FS.plot_mod(ax)
#ax.plot(np.linspace(1, 2E6, int(1E5)), modlim_inf*np.ones(int(1E5)), color="silver", alpha=0)
#ax.plot(np.linspace(1, 2E6, int(1E5)), modlim_sup*np.ones(int(1E5)), color="silver", alpha=0)
if plot_fo:
    ax.axvline(fo, color="red")
    ax.axhline(20 * np.log10(GI) - 3, color="red")
FS.plot_ph(ax2)
if plot_fo:
    ax2.axvline(fo, color="red")
    ax2.axhline(-45, color="red")
fig.tight_layout()
# plt.savefig(TS.title + ".jpg", dpi=300)
plt.show()

