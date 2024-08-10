import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Parameters: Poisson Distributions
lambda_1 = 1
lambda_2 = 5
lambda_3 = 10
lambda_4 = 45

x1 = np.arange(100)
x2 = np.arange(100)
x3 = np.arange(100)
x4 = np.arange(100)

pmf_x1 = poisson.pmf(x1, lambda_1)
pmf_x2 = poisson.pmf(x2, lambda_2)
pmf_x3 = poisson.pmf(x3, lambda_3)
pmf_x4 = poisson.pmf(x4, lambda_4)

# Cartesian plane setup
fig, ax = plt.subplots()

ax.set_title('Poisson Distributions')

ax.set_xlabel('')
ax.set_xticks(np.arange(0, 100, 5))
ax.set_xticks(np.arange(0, 100), minor=True)
ax.set_xlim(-1, 67)

ax.set_ylabel('')

# Plot data
ax.plot(x1, pmf_x1, marker='o', linestyle=':', color='red'   , alpha=0.5,
        label='X1~Poiss(λ=1)')
ax.plot(x2, pmf_x2, marker='o', linestyle=':', color='green' , alpha=0.5,
        label='X2~Poiss(λ=5)')
ax.plot(x3, pmf_x3, marker='o', linestyle=':', color='blue'  , alpha=0.5,
        label='X3~Poiss(λ=10)')
ax.plot(x4, pmf_x4, marker='o', linestyle=':', color='orange', alpha=0.5,
        label='X4~Poiss(λ=45)')

# Render
ax.grid()
ax.legend()

plt.show()
