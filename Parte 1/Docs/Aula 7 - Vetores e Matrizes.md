# Álgebra Linear

## Vetores e Matrizes

### Espaço Vetorial
O **espaço vetorial** é um conjunto de vetores onde operações de adição e multiplicação por escalares são definidas. Para um conjunto de vetores ser considerado um espaço vetorial, ele deve satisfazer propriedades como fechamento, existência de um elemento neutro e simétrico para a adição, entre outras.

### Representação Vetorial
- Vetores no espaço **R²** e **R³** são comumente usados em álgebra linear.
- Vetores podem ser representados como combinações lineares de vetores de uma **base**, como a base canônica em R²: {e1, e2}, onde e1 = [1, 0] e e2 = [0, 1].
- Em termos práticos, os vetores são listados como colunas ou linhas para facilitar operações com matrizes.

### Operações com Matrizes
- **Cálculo com Matrizes** envolve multiplicação, adição e operações de transposição.
- A **matriz transposta** é obtida ao inverter linhas e colunas de uma matriz original.
- Quando uma matriz é multiplicada pela sua transposta (assumindo uma matriz ortogonal), o resultado é a matriz identidade: 
  \[ A^T \times A = I \].

### Conversão de Equações para Notação Matricial
Equações lineares podem ser representadas por **matrizes**, facilitando a resolução de sistemas e o uso em algoritmos.

#### Exemplo
Se temos uma equação:
\[ y = h6 \cdot w68 + h7 \cdot w78 + b8 \]
podemos reescrevê-la em notação matricial como:
\[
\begin{bmatrix} W68 & W78 \end{bmatrix} \begin{bmatrix} h6 \\ h7 \end{bmatrix} + \begin{bmatrix} b8 \end{bmatrix} = \begin{bmatrix} y \end{bmatrix}
\]
onde:
- A primeira matriz, **[W68 W78]**, representa os pesos,
- A segunda matriz, **[h6, h7]** representa os valores de entrada,
- E a terceira, **[b8]**, é o termo de **bias**.

Essa notação simplifica a escrita e manipulação de várias equações, permitindo resolver sistemas lineares de forma mais eficaz e estender o conceito para redes neurais e computação vetorial.

