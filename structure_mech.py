# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

gzi_array = np.arange(-1, 1, 0.01)
rambda = 100
P = 1
l = 1
S1_array = 0.5*P + P*np.sinh((gzi_array*rambda**0.5)) / (2*l*np.sinh(rambda**0.5))
S2_array = 0.5*P - P*np.sinh((gzi_array*rambda**0.5)) / (2*l*np.sinh(rambda**0.5))
tau_array = P*np.cosh(gzi_array*rambda**0.5)/(2*l*np.sinh(rambda**0.5))

plt.plot(gzi_array, S1_array)
plt.plot(gzi_array, S2_array)
plt.plot(gzi_array, tau_array)
plt.title("λ = 100")
plt.show()