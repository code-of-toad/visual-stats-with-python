"""
NOTE: N = Population size
      n = Sample size
      D = Number of successes out of the population
      x = Number of successes out of the sample
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import hypergeom

# Parameters: Hypergeometric Distribution
N1 = 100
N2 = 100
N3 = 100
N4 = 100

n1 = 15
n2 = 15
n3 = 25
n4 = 25

D1 = 30
D2 = 60
D3 = 40
D4 = 80

x1 = np.arange(n1 + 1)
x2 = np.arange(n2 + 1)
x3 = np.arange(n3 + 1)
x4 = np.arange(n4 + 1)

pmf_x1 = hypergeom.pmf(x1, N1, D1, n1)
pmf_x2 = hypergeom.pmf(x2, N2, D2, n2)
pmf_x3 = hypergeom.pmf(x3, N3, D3, n3)
pmf_x4 = hypergeom.pmf(x4, N4, D4, n4)

# Cartesian plane setup
fig, ax = plt.subplots()

ax.set_title('Hypergeometric Distributions')

ax.set_xlabel('Number of successes within the sample')
ax.set_xticks(np.arange(0, 31, 5))
ax.set_xticks(np.arange(0, 31), minor=True)
ax.set_xlim(-1, 27)

ax.set_ylabel('P (X successes occur within the sample)')

# Plot data
ax.plot(x1, pmf_x1, marker='o', linestyle=':', color='red',    alpha=0.6,
        label='X1~Hypergeo(N=100, D=30, n=15)')
ax.plot(x2, pmf_x2, marker='o', linestyle=':', color='green',  alpha=0.6,
        label='X2~Hypergeo(N=100, D=60, n=15)')
ax.plot(x3, pmf_x3, marker='o', linestyle=':', color='blue',   alpha=0.6,
        label='X3~Hypergeo(N=100, D=40, n=25)')
ax.plot(x4, pmf_x4, marker='o', linestyle=':', color='orange', alpha=0.6,
        label='X4~Hypergeo(N=100, D=80, n=25)')

# Render
ax.grid()
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15))

plt.tight_layout()
plt.show()

