import numpy as np
import matplotlib.pyplot as plt


# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Function to calculate the electric field of a point charge
def electric_field(charge_pos, observation_pos):
    r = observation_pos - charge_pos
    r_mag = np.linalg.norm(r)
    k = 15  # Electric constant
    E = k * r / r_mag**3
    return E

# Create a 3D grid with reduced resolution
x = np.arange(-10, 10, 1.99)
y = np.arange(-10, 10, 1.99)
z = np.arange(-10, 10, 1.99)
X, Y, Z = np.meshgrid(x, y, z)

# Select a subset of points from the grid
sample_rate = 2  # Sampling frequency
X = X[::sample_rate, ::sample_rate, ::sample_rate]
Y = Y[::sample_rate, ::sample_rate, ::sample_rate]
Z = Z[::sample_rate, ::sample_rate, ::sample_rate]

# List of charges
charges = []

# Function to add an electric charge at a given position
def add_charge(charge_value, x, y, z):
    charge_pos = np.array([x, y, z])
    charges.append((charge_value, charge_pos))

# Use the function to add electric charges (+/-e) at positions (x,y,z)
add_charge(1, -2,0,0)
add_charge(-1, 2,0,0)


# Update the electric field based on all charges
E_x = np.zeros_like(X)
E_y = np.zeros_like(Y)
E_z = np.zeros_like(Z)

for charge_value, charge_pos in charges:
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            for k in range(X.shape[2]):
                observation_pos = np.array([X[i, j, k], Y[i, j, k], Z[i, j, k]])
                E = electric_field(charge_pos, observation_pos)
                E_x[i, j, k] += E[0] * charge_value
                E_y[i, j, k] += E[1] * charge_value
                E_z[i, j, k] += E[2] * charge_value

# Calculate the color of arrows based on the nearest charge
colors = []
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        for k in range(X.shape[2]):
            observation_pos = np.array([X[i, j, k], Y[i, j, k], Z[i, j, k]])
            distances = [np.linalg.norm(charge_pos - observation_pos) for _, charge_pos in charges]
            closest_distance = min(distances)
            closest_charge = charges[distances.index(closest_distance)]
            
            # Calculate the gradual color based on the charge
            alpha = (-closest_charge[0] + 1) / 2.0  # From -1 (blue) to 1 (red)
            color = (1 - alpha, 0, alpha)  # Gradual color from blue to red
            
            colors.append(color)

# Plot the electric field arrows
ax.quiver(X, Y, Z, E_x, E_y, E_z, color=colors, length=1, normalize=True)

# Display the charges
for charge_value, charge_pos in charges:
    color = 'blue' if charge_value < 0 else 'red'
    ax.scatter(charge_pos[0], charge_pos[1], charge_pos[2], color=color, s=50, label='Charge' + (' negative' if charge_value < 0 else ' positive'))

# Axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Graph title
plt.title("Electric Field Lines in 3D with Point Charges")

# Display the legend
ax.legend()

# Show the plot
plt.show()
