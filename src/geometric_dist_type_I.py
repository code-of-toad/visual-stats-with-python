"""
NOTE: The Type I variant of the Geometric Distribution counts
      trials until success -- not failures.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom

# Parameters: Geometric Distributions (Type I)
p1 = 0.20
p2 = 0.50
p3 = 0.80
p4 = 1.00

x1 = np.arange(1, 40)
x2 = np.arange(1, 40)
x3 = np.arange(1, 40)
x4 = np.arange(1, 40)

pmf_x1 = geom.pmf(k=x1, p=p1)
pmf_x2 = geom.pmf(k=x2, p=p2)
pmf_x3 = geom.pmf(k=x3, p=p3)
pmf_x4 = geom.pmf(k=x4, p=p4)

# Cartesian plane setup
fig, ax = plt.subplots()
ax.set_title('Geometric Distributions (Type I)')

ax.set_xlabel('Number of trials until the first success')
ax.set_xticks([x for x in range(1, 21)])
ax.set_xlim(0, 21)

ax.set_ylabel('P (X trials until the first success)')

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
