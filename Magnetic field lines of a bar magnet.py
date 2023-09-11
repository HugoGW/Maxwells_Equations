import numpy as np
import matplotlib.pyplot as plt

# Magnetic constant
mu0 = 4 * np.pi * 1e-7  # Permeability of free space

# Function to calculate the magnetic field of a bar magnet
def magnetic_field(magnet_moment, observation_pos, magnet_pos):
    r = observation_pos - magnet_pos
    r_mag = np.linalg.norm(r)
    r_unit = r / r_mag
    B = (mu0 / (4 * np.pi)) * (3 * (magnet_moment.dot(r_unit)) * r_unit - magnet_moment) / r_mag**3
    return B

# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Position of the bar magnet
magnet_pos = np.array([0, 0, 0])

# Magnetic moment of the bar magnet
magnet_moment = np.array([1, 0, 0])  # The bar magnet points in the z-direction

# Dimensions of the bar magnet (length, width, height)
magnet_dimensions = np.array([1, 0.2, 0.2])

# Create the wireframe representing the bar magnet in blue (South pole)
x_bar = np.linspace(-magnet_dimensions[0] / 2, magnet_dimensions[0] / 2, 100)
y_bar = np.linspace(-magnet_dimensions[1] / 2, magnet_dimensions[1] / 2, 100)
z_bar = np.linspace(-magnet_dimensions[2] / 2, magnet_dimensions[2] / 2, 100)
X_bar, Z_bar = np.meshgrid(x_bar, z_bar)
Y_bar = np.full_like(X_bar, 0.0)  # The bar is in the y=0 plane
ax.plot_wireframe(X_bar-(1/2), Y_bar-1/2, Z_bar, color='blue', label='South Pole')
ax.plot_wireframe(X_bar+(1/2), Y_bar-1/2, Z_bar, color='red', label='North Pole')

# Create a 3D grid with reduced resolution
x = np.arange(-5, 5, 1.8)
y = np.arange(-5, 5, 1.8)
z = np.arange(-5, 5, 1.8)
X, Y, Z = np.meshgrid(x, y, z)

# Calculate the magnetic field at each point in the grid
B_x = np.zeros_like(X)
B_y = np.zeros_like(Y)
B_z = np.zeros_like(Z)

for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        for k in range(X.shape[2]):
            observation_pos = np.array([X[i, j, k], Y[i, j, k], Z[i, j, k]])
            B = magnetic_field(magnet_moment, observation_pos, magnet_pos)
            B_x[i, j, k] = B[0]
            B_y[i, j, k] = B[1]
            B_z[i, j, k] = B[2]

# Plot the magnetic field lines
ax.quiver(X, Y, Z, B_x, B_y, B_z, length=0.5, color='gray', normalize=True)

# Axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Graph title
plt.title("Magnetic Field Lines of a Bar Magnet in 3D")

# Display the graph
plt.legend()
plt.show()
