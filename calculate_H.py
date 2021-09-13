import numpy as np
import scipy.signal as ss
import sympy as sp

########################################################################################################################
# draw_H: Dibuja la función transferencia provista
# Recibe el numerador y denominador de H
# ----------------------------------------------------------------------------------------------------------------------
def draw_H(num, den):
    num = num/num[-1]
    den = den/den[-1]
    w0 = den[0] ** (-1 / (len(den)-1))
    f0 = w0 / (2 * np.pi)
    n = f"\t \t"
    d = f"\t \t"
    for i in range(len(num)):
        n = n + f"{num[i]:3g}s^{len(num) - 1 - i}"
        if i != len(num) - 1:
            n = n + f" + "
    print(n)
    #print(f"\t \t  {num[0]:3g}s^3 + {num[1]:3g}s^2 + {num[2]:3g}s + {num[3]}")
    print("H(s) = -------------------------------------------------------------")
    for i in range(len(den)):
        d = d + f"{den[i]:3g}s^{len(den) - 1 - i}"
        if i != len(den) - 1:
            d = d + f" + "
    print(d)
    #print(f"\t \t {den[0]:3g}s^3 + {den[1]:3g}s^2 + {den[2]:3g}s + {den[3]}")
    print(f"w0 = {w0} rad/s => f0 = {f0} Hz")
    return
########################################################################################################################

########################################################################################################################
# normalize_H: Normaliza la función transferencia provista tal que el término independiente sea 1
# Recibe el numerador y denominador de H
# Devuelve el numerador y denominador de H normalizada
# ----------------------------------------------------------------------------------------------------------------------
def normalize_H(num, den):
    s = sp.symbols('s')
    num_roots = sp.nroots(num[0]*s**3 + num[1]*s**2 + num[2]*s + num[3])
    den_roots = sp.nroots(den[0]*s**3 + den[1]*s**2 + den[2]*s + den[3])
    num = np.array([num[0], -num[0]*(sp.re(num_roots[1]) + sp.im(num_roots[1])*1j + sp.re(num_roots[2]) + sp.im(num_roots[2])*1j), num[0]*np.abs((sp.re(num_roots[1]) + sp.im(num_roots[1])*1j))**2])
    den = np.array([den[0], -den[0]*(den_roots[0] + den_roots[2]), den[0]*den_roots[0]*den_roots[2]])
    return num, den
########################################################################################################################
