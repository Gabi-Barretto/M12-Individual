# Autovalores e Autovetores

Em álgebra linear, um **autovetor** de uma matriz \( A \) é um vetor que, ao ser transformado por \( A \), resulta em um vetor colinear ao vetor inicial. O **autovalor** associado é o fator de escala (lambda, \( \lambda \)) que multiplica o autovetor nessa transformação.

A relação fundamental para autovalores e autovetores é dada pela equação:
\[
A \vec{x} = \lambda \vec{x}
\]
onde:
- \( A \) é a matriz de transformação,
- \( \lambda \) é o autovalor,
- \( \vec{x} \) é o autovetor associado a \( \lambda \).

### Passos para Encontrar Autovalores e Autovetores

1. **Calcule o determinante da matriz característica**:
   Para encontrar os autovalores, começamos da equação:
   \[
   (A - \lambda I) \vec{x} = 0
   \]
   onde \( I \) é a matriz identidade. Para que essa equação tenha soluções não triviais (ou seja, para que \( \vec{x} \neq 0 \)), o determinante da matriz \( A - \lambda I \) deve ser zero:
   \[
   \det(A - \lambda I) = 0
   \]
   
2. **Determine os autovalores (\( \lambda \)) resolvendo o polinômio característico**:
   Substituímos os valores de \( A \) e \( I \) na expressão e resolvemos o determinante. Esse procedimento nos fornece um polinômio em \( \lambda \), chamado de polinômio característico. As raízes desse polinômio são os autovalores da matriz.

3. **Encontre os autovetores associados**:
   Para cada autovalor \( \lambda \), substituímos em \( (A - \lambda I) \vec{x} = 0 \) e resolvemos o sistema linear para encontrar os autovetores associados.

---

### Exemplo

Considere a matriz:
\[
A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}
\]

1. **Calcule o determinante da matriz característica**:
   \[
   A - \lambda I = \begin{pmatrix} 1 - \lambda & 2 \\ 2 & 4 - \lambda \end{pmatrix}
   \]
   Calculamos o determinante:
   \[
   \det(A - \lambda I) = (1 - \lambda)(4 - \lambda) - 4 = \lambda^2 - 5\lambda = 0
   \]
   Resolvendo a equação, obtemos:
   \[
   \lambda_1 = 0 \quad \text{e} \quad \lambda_2 = 5
   \]

2. **Encontre os autovetores associados**:

   - Para \( \lambda = 0 \):
     \[
     (A - 0 \cdot I) \vec{x} = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix} \begin{pmatrix} a \\ b \end{pmatrix} = 0
     \]
     Resolvendo o sistema, obtemos \( a = -2b \), então um autovetor associado a \( \lambda = 0 \) é:
     \[
     \vec{x}_1 = b \begin{pmatrix} -2 \\ 1 \end{pmatrix}
     \]
     Podemos escolher \( b = 1 \) para simplificar, então \( \vec{x}_1 = \begin{pmatrix} -2 \\ 1 \end{pmatrix} \).

   - Para \( \lambda = 5 \):
     \[
     (A - 5 \cdot I) \vec{x} = \begin{pmatrix} -4 & 2 \\ 2 & -1 \end{pmatrix} \begin{pmatrix} a \\ b \end{pmatrix} = 0
     \]
     Resolvendo o sistema, obtemos \( b = 2a \), então um autovetor associado a \( \lambda = 5 \) é:
     \[
     \vec{x}_2 = a \begin{pmatrix} 1 \\ 2 \end{pmatrix}
     \]
     Podemos escolher \( a = 1 \), então \( \vec{x}_2 = \begin{pmatrix} 1 \\ 2 \end{pmatrix} \).

3. **Versores dos Autovetores**:
   Podemos normalizar os autovetores para obter os versores correspondentes:
   - Para \( \vec{x}_1 = \begin{pmatrix} -2 \\ 1 \end{pmatrix} \):
     \[
     \vec{u}_1 = \frac{\vec{x}_1}{\|\vec{x}_1\|} = \frac{1}{\sqrt{5}} \begin{pmatrix} -2 \\ 1 \end{pmatrix}
     \]

   - Para \( \vec{x}_2 = \begin{pmatrix} 1 \\ 2 \end{pmatrix} \):
     \[
     \vec{u}_2 = \frac{\vec{x}_2}{\|\vec{x}_2\|} = \frac{1}{\sqrt{5}} \begin{pmatrix} 1 \\ 2 \end{pmatrix}
     \]

---

Esses versores representam a direção dos autovetores associados aos autovalores \( \lambda = 0 \) e \( \lambda = 5 \), com magnitude unitária.
