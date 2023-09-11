import numpy as np
import matplotlib.pyplot as plt

# Create a 3D grid
x = np.arange(-2, 2.5, 0.8)
y = np.arange(-2, 2.5, 0.8)
z = np.arange(-2, 2.5, 0.8)
X, Y, Z = np.meshgrid(x, y, z)

# Position of the current loop (source of the magnetic field)
loop_x = 0.0
loop_y = 0.0
loop_z = 0.0

T = 0.5
omega = 2*np.pi/T  # Frequency of variation

# Physical parameters
mu_0 = 4 * np.pi * 1e-7  # Permeability of vacuum
epsilon_0 = 8.854187817e-12  # Permittivity of vacuum

# Define a function for the current density J in 3D (arbitrary)
def current_density(x, y, z, t):
    # For example, a sinusoidal wave propagating in the x-direction
    J_x = np.sin(omega * t) * np.exp(-((x - loop_x)**2 + (y - loop_y)**2 + (z - loop_z)**2))
    J_y = np.zeros_like(x)
    J_z = np.zeros_like(x)
    return J_x, J_y, J_z

# Calculate the components of the magnetic field in 3D
def magnetic_field(x, y, z, t):
    J_x, J_y, J_z = current_density(x, y, z, t)
    
    r_x = x - loop_x
    r_y = y - loop_y
    r_z = z - loop_z
    r = np.sqrt(r_x**2 + r_y**2 + r_z**2)
    
    # Magnetic field intensity (varies with time)
    B0 = 2.0
    B = B0 * np.sin(omega * t) / (2 * np.pi * r)
    
    # Direction of the magnetic field in 3D
    B_x = B * (-r_y / r)
    B_y = B * (r_x / r)
    B_z = B * np.sin(omega * t) / (2 * np.pi * r)
    
    return B_x, B_y, B_z

# Create an animation to visualize the evolution of the magnetic field in 3D
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
t_values = np.arange(0, 100, 0.02)

for t in t_values:
    B_x, B_y, B_z = magnetic_field(X, Y, Z, t)
    
    # Draw the magnetic field in 3D with labels
    ax.quiver(X, Y, Z, B_x, B_y, B_z, color='green', alpha=1, label='Magnetic Field (B)')
    
    # Add an arrow indicating the temporal variation of the field
    ax.quiver(0, 0, 0, 0, 0, np.sin(omega * t), color='blue', alpha=1, label='Eletric field (E)')
    
    # Add the current density in 3D with a label
    J_x, J_y, J_z = current_density(X, Y, Z, t)
    ax.quiver(X, Y, Z, J_x, J_y, J_z, color='red', alpha=0.5, label='Current Density (J)')
    
    # Display settings
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Maxwell-Ampère Equation Visualization in 3D')
    
    # Legend for labels
    ax.legend()

    plt.pause(0.001)
    ax.clear()

plt.show()
