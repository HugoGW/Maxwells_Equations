import numpy as np
import matplotlib.pyplot as plt

# Create a 2D grid
x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)

# Position of the current loop (source of the magnetic field)
loop_x = 0.0
loop_y = 0.0

T = 1
ε_0 = 1
µ_0 = 1
c = 1/np.sqrt(ε_0*µ_0)
J_0 = 1
E0 = 1

omega = 2.0 * np.pi/T  # Frequency of variation

# Calculate the components of the magnetic field
def electric_field(x, y, t):
    r_x = x - loop_x
    r_y = y - loop_y
    r = np.sqrt(r_x**2 + r_y**2)
    
    # Magnetic field intensity (varies with time)
    E = J_0 / (2 * np.pi * ε_0* r) * np.sin(omega * t)
    
    # Direction of the magnetic field
    E_x = E * (r_x / r)
    E_y = E * (r_y / r)
    
    return E_x, E_y

# Define a function for the current density J in 2D with z-component (arbitrary)
def current_density(x, y, t):
    # For example, a Gaussian function for the current density along the z-axis
    J_0 = 1
    J_x = np.zeros_like(x)
    J_y = np.zeros_like(y)
    J_z = J_0 * np.sin(omega * t)
    return J_x, J_y, J_z

# Calculate the components of the electric field
def magnetic_field(x, y, t):
    r_x = x - loop_x
    r_y = y - loop_y
    r = np.sqrt(r_x**2 + r_y**2)
    
    # Magnetic field intensity (varies with time)
    E = J_0 / (2 * np.pi * ε_0* r) * np.sin(omega * t)
    
    # Direction of the magnetic field
    E_x = E * (r_x / r)
    E_y = E * (r_y / r)
    
    B_x = -E_y/c  # Same behavior as B
    B_y = E_x/c  # Same behavior as B
    return B_x, B_y

# Create an animation to visualize the evolution of the magnetic field, current density, and electric field
fig, ax = plt.subplots(figsize=(10, 10))
t_values = np.arange(0, 100, 0.02)
plt.figtext(0.82, 0.78, r'$\vec{B} ~ \parallel ~ \vec{u}_{\theta}$', fontsize=14)
plt.figtext(0.82, 0.74, r'$\vec{E} ~ \parallel ~ \vec{u}_r$', fontsize=14)
plt.figtext(0.24, 0.78, r'$\vec{J} ~ \parallel ~ \vec{u}_z$', fontsize = 14)

for t in t_values:
    E_x, E_y = electric_field(X, Y, t)
    
    
    # Draw the electric field (E) with the same behavior as B (orthogonal to B)
    E_x, E_y = electric_field(X,Y,t)
    ax.quiver(X, Y, E_x, E_y, scale=20, color='blue', alpha=0.5, label='Electric Field (E)')
    
    # Draw the magnetic field (B) in XY plane
    B_x, B_y = magnetic_field(X, Y, t)
    ax.quiver(X, Y, B_x, B_y, scale=20, color='green', alpha=0.5, label='Magnetic Field (B)')
    
    ax.quiver(-1.5, 1.5, 0, 0.5 * np.sin(omega * t), scale=10, color='red', alpha=0.5, label = 'current density')

    # Display settings
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Maxwell-Ampère Equation Visualization in 2D')
    
    # Legend for labels
    ax.legend()

    plt.pause(0.001)
    ax.clear()

plt.show()
