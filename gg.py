import numpy as np
from scipy.stats import hypergeom
import matplotlib.pyplot as plt

# Parámetros de la distribución hipergeométrica
N = 7  # Tamaño de la población
K = 2  # Número de componentes defectuosos en la población
n = 3  # Tamaño de la muestra

# Valores posibles de X (número de componentes defectuosos en la muestra)
x = np.arange(0, n+1)

# Distribución de probabilidad
probabilidades = hypergeom.pmf(x, N, K, n)

# Gráfica de la distribución de probabilidad
plt.figure(figsize=(10, 6))
plt.bar(x, probabilidades, color='blue', alpha=0.7)
plt.xlabel('Número de componentes defectuosos en la muestra')
plt.ylabel('Probabilidad')
plt.title('Distribución de probabilidad hipergeométrica (N=7, K=2, n=3)')
plt.grid(True)
plt.show()

# Probabilidad P(0 < X ≤ 2)
p_0_menos_X_menor_igual_2 = sum(probabilidades[1:3])

probabilidades, p_0_menos_X_menor_igual_2
