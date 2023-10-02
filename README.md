# Maxwell's Equations of electromagnetism animated
Few years ago, I studied the four Maxwell's equations, and they are among the four most beautiful equations in modern physics. However, the concepts of divergence and curl in vector analysis can be quite complex, so I challenged myself to animate these four equations to plot the corresponding field lines visually. Indeed, a picture is worth a thousand words, so visualizing the operation of these four equations helps us better understand the resulting phenomena.

For the first equation named "Maxwell's Gauss Law", we have :

\begin{itemize}[label=\textbullet, font=\Large]
    $\displaystyle \vec{\nabla} \cdot \vec{E} = \frac{\rho}{\varepsilon_0}$
\end{itemize}


which means an electric charge is a source of the electric field.
In the code I've created, we observe the electric field lines (normalized). You can add a charge using the 'add_charge(q, x, y, z)' function, which takes as input:

\begin{itemize}
    \item $q = {\pm n e}$ for all $n \in \mathbb{N}^*$, representing the electric charge.
    \item $x, y, z$, the coordinates where you want to place the charge.
\end{itemize}

I made sure that the color of the field lines adapts to the value of the electric charge.


<img width="410" alt="+e" src="https://github.com/HugoGW/Maxwells_Equations/assets/140922475/10f034dd-84b5-48f8-934d-cbaad4456c98"> 
<img width="394" alt="-e" src="https://github.com/HugoGW/Maxwells_Equations/assets/140922475/eefad147-c3a0-4ade-a508-a1f3b1e950ed">
<img width="376" alt="+-e" src="https://github.com/HugoGW/Maxwells_Equations/assets/140922475/99fa5c16-c02d-4f7e-bc21-5b1e622fd9ca">

You can add any desired number of electric charges and place them wherever you want. \\\\



For the second equation called "Maxwell's Thomson Law", we have :

\begin{itemize}[label=\textbullet, font=\Large]
    $\displaystyle \vec{\nabla} \cdot \vec{B} = 0$
\end{itemize}


This means that the field lines loop back onto themselves. In other words, there are no magnetic monopoles; only magnetic dipoles exist.

<img width="417" alt="dipole magnétique" src="https://github.com/HugoGW/Maxwells_Equations/assets/140922475/2eaafa07-026a-43ed-9feb-28c9b708893a"> \\\\


The third equation, known as "Maxwell's Faraday Law", lays the foundation for what we call electromagnetic induction. Indeed, if we consider time-varying electric and magnetic fields, then we have $\displaystyle \vec{\nabla} \wedge \vec{E} = - \frac{\partial \vec{B}}{\partial t}$. This means that a time-varying magnetic field will induce a time-varying electric field in space, rotating around the magnetic field. To visualize this phenomenon, I created simulations in 2D and 3D.

