import numpy as np
import matplotlib.pyplot as plt

# Create a 2D grid
x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)

# Position of the current loop (source of the magnetic field)
loop_x = 0.0
loop_y = 0.0

omega = 2.0 * np.pi  # Frequency of variation

# Calculate the components of the electric field
def electric_field(x, y, t):
    r_x = x - loop_x
    r_y = y - loop_y
    r = np.sqrt(r_x**2 + r_y**2)
    
    # Electric field intensity (varies with time)
    E0 = 1.0
    E = E0 * np.sin(omega * t) / (2 * np.pi * r)
    
    # Direction of the electric field
    E_x = E * (-r_y / r)
    E_y = E * (r_x / r)
    
    return E_x, E_y

# Create an animation to visualize the evolution of the electric field and the magnetic field
fig, ax = plt.subplots(figsize=(10, 10))
t_values = np.arange(0, 100, 0.02)
plt.figtext(0.82, 0.78, r'$\vec{B} ~ \parallel ~ \vec{u}_z$', fontsize=14)
plt.figtext(0.82, 0.74, r'$\vec{E} ~ \perp ~ \vec{B}$', fontsize=14)

for t in t_values:
    E_x, E_y = electric_field(X, Y, t)
    
    # Draw the electric field lines in 2D
    ax.quiver(X, Y, E_x, E_y, scale=20, color='blue', alpha=0.5, label='Electric Field (E)')
    
    # Add an arrow indicating the temporal variation of the magnetic field
    ax.quiver(1.5, 1.5, 0, 0.5 * np.sin(omega * t), scale=10, color='green', alpha=1, label='Magnetic Field (B)')
    
    # Display settings
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Maxwell-Faraday Equation Visualization in 2D')
    
    # Set equal aspect ratio for x and y axes
    ax.set_aspect('equal')
    
    # Legend for labels
    ax.legend()

    plt.pause(0.001)
    ax.clear()

plt.show()
