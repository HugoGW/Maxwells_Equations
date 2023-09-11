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
omega = 2 * np.pi / T  # Frequency of variation

# Calculate the components of the magnetic field in 3D
def electric_field(x, y, z, t):
    r_x = x - loop_x
    r_y = y - loop_y
    r_z = z - loop_z
    r = np.sqrt(r_x**2 + r_y**2 + r_z**2)
    
    # Magnetic field intensity (varies with time)
    B0 = 2.0
    B = B0 * np.sin(omega * t) / (2 * np.pi * r)
    
    # Direction of the magnetic field in 3D
    E_x = B * (-r_y / r)
    E_y = B * (r_x / r)
    E_z = B * np.sin(omega * t) / (2 * np.pi * r)
    
    return E_x, E_y, E_z

# Create an animation to visualize the evolution of the magnetic field in 3D
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
t_values = np.arange(0, 100, 0.015)

for t in t_values:
    E_x, E_y, E_z = electric_field(X, Y, Z, t)
    
    # Draw the magnetic field lines in 3D
    ax.quiver(X, Y, Z, E_x, E_y, E_z, color='blue', alpha=1, label='Electric field (E)')
    
    # Add an arrow indicating the temporal variation of the magnetic field
    ax.quiver(0, 0, 0, 0, 0, np.sin(omega * t), color='green', alpha=1, label='Magnetic field (B)')
    
    # Display settings
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Maxwell-Faraday Equation Visualization in 3D')
    
    # Legend for labels
    ax.legend()

    plt.pause(0.001)
    ax.clear()

plt.show()
