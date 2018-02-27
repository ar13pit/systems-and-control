************
Optimization
************


.. math::
   \underbrace{
   \left[
   \begin{array}{c|c}
      A_1 & B_1 \\ \hline
      C_1 & D_1
   \end{array}
   \right]}_{\Sigma_1} .   \underbrace{\left[
   \begin{array}{c|c}
      A_2 & B_2 \\ \hline
      C_2 & D_2
   \end{array}
   \right]}_{\Sigma_2} =    \left[
      \begin{array}{cc|c}
         A_1 & B_1C_2 & B_1D_2 \\
         0 & A_2 & B_2 \\ \hline
         C_1 & D_1C_2 & D_1D_2
      \end{array}
      \right]

.. math::
   \left[
   \begin{array}{cccc|c}
      1 & 0 & 3 & -1 & 0 \\
      0 & 1 & 1 & -1 & 0 \\ \hline
      0 & 0 & 0 & 0 & 0 \\
   \end{array}
   \right]
