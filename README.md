# Maxwell's Equations of electromagnetism animated
Few years ago, I studied the four Maxwell's equations, and they are among the four most beautiful equations in modern physics. However, the concepts of divergence and curl in vector analysis can be quite complex, so I challenged myself to animate these four equations to plot the corresponding field lines visually. Indeed, a picture is worth a thousand words, so visualizing the operation of these four equations helps us better understand the resulting phenomena.

For the first equation named 'Maxwell's Gauss Law,' we have $\vec{\nabla} \cdot \vec{E} = \frac{\rho}{\varepsilon_0}$, which means an electric charge is a source of the electric field.
In the code I've created, we observe the electric field lines (normalized). You can add a charge using the 'add_charge(q, x, y, z)' function, which takes as input:

$q = {\pm n e}$ for all $n \in \mathbb{N}^*$, representing the electric charge.
$x, y, z$, the coordinates where you want to place the charge.

You can add any desired number of electric charges.
