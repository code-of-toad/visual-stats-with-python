import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from pprint import pprint

# Parameters: Binomial Distribution
n1 = 20
n2 = 20
n3 = 20

p1 = 0.15
p2 = 0.50
p3 = 0.85

x1 = np.arange(0, n1 + 1)
x2 = np.arange(0, n2 + 1)
x3 = np.arange(0, n3 + 1)

pmf_x1 = binom.pmf(k=x1, n=n1, p=p1)
pmf_x2 = binom.pmf(k=x2, n=n2, p=p2)
pmf_x3 = binom.pmf(k=x3, n=n3, p=p3)

# Cartesian plane setup
fig, ax = plt.subplots()

ax.set_title('Binomial Distributions')

ax.set_xlabel('# Successes out of n trials')
ax.set_xticks([x for x in range(21)])
ax.set_xlim(-1, 21)

ax.set_ylabel('P (Exactly X successes occur)')

# Plot the Distributions
ax.bar(x1, pmf_x1, color='r', alpha=0.6, align='center', label='X1~Binom(n=20, p=0.15)')
ax.bar(x2, pmf_x2, color='g', alpha=0.6, align='center', label='X2~Binom(n=20, p=0.50)')
ax.bar(x3, pmf_x3, color='b', alpha=0.6, align='center', label='X3~Binom(n=20, p=0.85)')

# Render
ax.grid()
ax.legend()

plt.show()
