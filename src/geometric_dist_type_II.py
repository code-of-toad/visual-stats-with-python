"""
NOTE: The Type II variant of the Geometric Distribution counts
      failures until success -- not trials.
"""
import numpy as np
import matplotlib.pyplot as plt
from numpy.typing import NDArray

# Custom function 
def geom_type2_pmf(support: NDArray, p: float) -> NDArray:
    geom = lambda x, prob: prob * (1 - prob) ** x
    array = np.empty((len(support),), dtype=float)
    for i in range(len(support)):
        array[i] = geom(i, p)
    return array

# Parameters: Geometric Disribution (Type II)
p1 = 0.20
p2 = 0.50
p3 = 0.80
p4 = 1.00

x1 = np.arange(40)
x2 = np.arange(40)
x3 = np.arange(40)
x4 = np.arange(40)

pmf_x1 = geom_type2_pmf(x1, p1)
pmf_x2 = geom_type2_pmf(x2, p2)
pmf_x3 = geom_type2_pmf(x3, p3)
pmf_x4 = geom_type2_pmf(x4, p4)

# Cartesian plane setup
fig, ax = plt.subplots()

ax.set_title('Geometric Distributions (Type II)')

ax.set_xlabel('# Failures before the first success')
ax.set_xticks([x for x in range(21)])
ax.set_xlim(-1, 21)

ax.set_ylabel('P (X failures occur before the first success)')

# Plot data
ax.plot(x1, pmf_x1, marker='o', linestyle=':', color='red',    alpha=0.6,
        label='X1~Geo(p=0.2)')
ax.plot(x2, pmf_x2, marker='o', linestyle=':', color='green',  alpha=0.6,
        label='X2~Geo(p=0.5)')
ax.plot(x3, pmf_x3, marker='o', linestyle=':', color='blue',   alpha=0.6,
        label='X3~Geo(p=0.8)')
ax.plot(x4, pmf_x4, marker='o', linestyle=':', color='orange', alpha=0.6,
        label='X4~Geo(p=1.0)')

# Render
ax.grid()
ax.legend()

plt.show()

