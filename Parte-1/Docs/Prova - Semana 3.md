## 1. Escalares, Vetores e Matrizes

### Definições e Operações Básicas
   - **Escalares**: São números que multiplicam vetores e matrizes, atuando como fatores de escala. Em redes neurais, os pesos são escalares que multiplicam valores das entradas, ajustando a influência de cada dado.
   - **Vetores**: Listas ordenadas de números, representando dados multidimensionais. Em machine learning, são usados para armazenar características, como intensidade de pixels em uma imagem.
     - **Soma de Vetores**: Para dois vetores \(\vec{u} = (u_1, u_2, \dots, u_n)\) e \(\vec{v} = (v_1, v_2, \dots, v_n)\), a soma é \(\vec{u} + \vec{v} = (u_1 + v_1, u_2 + v_2, \dots, u_n + v_n)\).
     - **Produto por Escalar**: Um vetor \(\vec{v} = (v_1, v_2, \dots, v_n)\) multiplicado por um escalar \(\alpha\) resulta em \(\alpha \vec{v} = (\alpha v_1, \alpha v_2, \dots, \alpha v_n)\).
   - **Matrizes**: Estruturas bidimensionais essenciais para representar transformações lineares. Em redes neurais, as matrizes multiplicam vetores de entrada para gerar novas representações dos dados.
     - **Multiplicação de Matrizes**: Para duas matrizes \(A\) (dimensão \(m \times n\)) e \(B\) (\(n \times p\)), a multiplicação \(C = A \cdot B\) resulta em uma matriz \(C\) (dimensão \(m \times p\)), com cada elemento \(c_{ij}\) dado por \(\sum_{k=1}^{n} a_{ik} \cdot b_{kj}\).

### Exemplo Real e Cenário de Prova
   - **Exemplo Real**: Em uma rede neural que classifica dígitos manuscritos, cada imagem é representada como um vetor de características (intensidade dos pixels). Com a matriz de pesos:
     \[
     A = \begin{bmatrix} 1 & 0 & 2 \\ 0 & 1 & 1 \\ 1 & 1 & 0 \end{bmatrix}
     \]
     e o vetor de entrada \(\vec{x} = (3, 5, 7)\), a multiplicação resulta em:
     \[
     A \cdot \vec{x} = \begin{bmatrix} 17 \\ 12 \\ 8 \end{bmatrix}
     \]
   - **Cenário de Prova**: Um enunciado poderia solicitar que o aluno demonstre a multiplicação de matrizes no contexto de uma rede neural, explicando como cada passo contribui para a transformação dos dados.

---

## 2. Autovalores e Autovetores

### Definições Matemáticas e Propriedades
   - Um vetor \(\vec{x}\) é um autovetor de uma matriz \(A\) se, ao ser transformado por \(A\), ele é multiplicado por um escalar, mantendo a mesma direção: \(A\vec{x} = \lambda \vec{x}\), onde \(\lambda\) é o autovalor correspondente.
   - **Equação Característica**: Para encontrar autovalores, resolvemos o polinômio característico \( \det(A - \lambda I) = 0 \), onde \(I\) é a matriz identidade. As raízes desse polinômio são os autovalores.
   - **Autovetores**: Para cada autovalor \(\lambda\), resolvemos o sistema \( (A - \lambda I) \vec{x} = 0 \) para encontrar os autovetores correspondentes.

### Exemplo Real e Cenário de Prova
   - **Exemplo Real**: Em uma análise de estabilidade financeira, autovalores ajudam a prever a tendência de crescimento ou declínio de um sistema. Com a matriz:
     \[
     A = \begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix}
     \]
     encontramos os autovalores \(\lambda_1 = 5\) e \(\lambda_2 = 2\) e os autovetores correspondentes, \(\vec{x}_1 = (1, 2)\) e \(\vec{x}_2 = (-1, 1)\).
   - **Cenário de Prova**: O aluno poderia ser solicitado a calcular autovalores e autovetores de uma matriz financeira, interpretando como essas propriedades revelam tendências de crescimento ou estabilidade.

---

## 3. Transformações Lineares

### Definição
   - Uma transformação linear é uma função \( T: V \rightarrow W \) que preserva operações de adição e multiplicação por escalar. Para vetores \(\vec{u}\) e \(\vec{v}\) em \(V\) e escalar \(\alpha\):
     - \( T(\vec{u} + \vec{v}) = T(\vec{u}) + T(\vec{v}) \)
     - \( T(\alpha \vec{u}) = \alpha T(\vec{u}) \)
   - **Matriz de Transformação**: Para uma transformação \(T\) em \( \mathbb{R}^n \), existe uma matriz \(A\) tal que \(T(\vec{x}) = A \vec{x}\) para qualquer vetor \(\vec{x}\).

### Exemplo Real e Cenário de Prova
   - **Exemplo Real**: Em visão computacional, uma transformação de rotação de \(90^\circ\) no plano \(\mathbb{R}^2\) pode ser representada pela matriz:
     \[
     R = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}
     \]
     Aplicando essa transformação a \(\vec{v} = (2, 3)\), o resultado é \(\begin{bmatrix} -3 \\ 2 \end{bmatrix}\).
   - **Cenário de Prova**: O aluno poderia ser solicitado a calcular a transformação de um vetor sob uma rotação e interpretar o significado geométrico, aplicando conceitos de manipulação de imagem.

---

## 4. Diagonalização de Matrizes

### Definição e Processo
   - Uma matriz \(A\) é diagonalizável se existe uma matriz \(S\) de autovetores e uma matriz diagonal \(\Lambda\) de autovalores tal que \(A = S \Lambda S^{-1}\). Esse processo simplifica cálculos, especialmente em operações com potências de matrizes.
   - **Processo de Diagonalização**:
     - Encontrar autovalores e autovetores de \(A\).
     - Formar \(S\) com os autovetores e \(\Lambda\) com os autovalores na diagonal.

### Cenário de Prova e Resposta
- **Cenário**: Dada a matriz \(A = \begin{bmatrix} 3 & 1 \\ 0 & 2 \end{bmatrix}\), verifique se ela é diagonalizável e, caso seja, encontre as matrizes \(S\) e \(\Lambda\) de tal forma que \(A = S \Lambda S^{-1}\).

### Resolução Completa
Para diagonalizar a matriz \(A\), seguimos estes passos:

1. **Encontrar os Autovalores**:
   - Começamos com a equação característica, \(\det(A - \lambda I) = 0\), onde \(I\) é a matriz identidade.
   - Subtraímos \(\lambda\) da diagonal de \(A\) e encontramos o determinante:
     \[
     A - \lambda I = \begin{bmatrix} 3 - \lambda & 1 \\ 0 & 2 - \lambda \end{bmatrix}
     \]
   - O determinante é calculado como:
     \[
     \det(A - \lambda I) = (3 - \lambda)(2 - \lambda) - (1 \cdot 0) = \lambda^2 - 5\lambda + 6 = 0
     \]
   - Resolvendo o polinômio quadrático \(\lambda^2 - 5\lambda + 6 = 0\), obtemos os autovalores:
     \[
     \lambda_1 = 3 \quad \text{e} \quad \lambda_2 = 2
     \]

2. **Encontrar os Autovetores**:
   - Para cada autovalor, resolvemos o sistema \((A - \lambda I) \vec{x} = 0\) para encontrar os autovetores associados.

   - **Para \(\lambda = 3\)**:
     - Substituímos \(\lambda = 3\) em \(A - \lambda I\):
       \[
       A - 3I = \begin{bmatrix} 3 - 3 & 1 \\ 0 & 2 - 3 \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ 0 & -1 \end{bmatrix}
       \]
     - O sistema de equações se reduz a:
       \[
       0 \cdot x_1 + 1 \cdot x_2 = 0 \Rightarrow x_2 = 0
       \]
       - Podemos escolher \(x_1 = 1\), então um autovetor correspondente a \(\lambda = 3\) é \(\vec{v}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}\).

   - **Para \(\lambda = 2\)**:
     - Substituímos \(\lambda = 2\) em \(A - \lambda I\):
       \[
       A - 2I = \begin{bmatrix} 3 - 2 & 1 \\ 0 & 2 - 2 \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 0 & 0 \end{bmatrix}
       \]
     - O sistema de equações se reduz a:
       \[
       1 \cdot x_1 + 1 \cdot x_2 = 0 \Rightarrow x_1 = -x_2
       \]
       - Escolhemos \(x_2 = 1\), então um autovetor correspondente a \(\lambda = 2\) é \(\vec{v}_2 = \begin{bmatrix} -1 \\ 1 \end{bmatrix}\).

3. **Formar as Matrizes \(S\) e \(\Lambda\)**:
   - Agora que temos os autovalores e autovetores, podemos formar as matrizes \(S\) e \(\Lambda\):
     - **Matriz \(S\)**: É composta pelos autovetores como colunas.
       \[
       S = \begin{bmatrix} 1 & -1 \\ 0 & 1 \end{bmatrix}
       \]
     - **Matriz Diagonal \(\Lambda\)**: Contém os autovalores na diagonal.
       \[
       \Lambda = \begin{bmatrix} 3 & 0 \\ 0 & 2 \end{bmatrix}
       \]

4. **Verificação**:
   - Para confirmar a diagonalização, verificamos se \(A = S \Lambda S^{-1}\).
   - Calculamos \(S^{-1}\):
     \[
     S = \begin{bmatrix} 1 & -1 \\ 0 & 1 \end{bmatrix} \Rightarrow S^{-1} = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}
     \]
   - Então:
     \[
     S \Lambda S^{-1} = \begin{bmatrix} 1 & -1 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 3 & 0 \\ 0 & 2 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 3 & 1 \\ 0 & 2 \end{bmatrix} = A
     \]

### Interpretação Final
Essa diagonalização mostra que podemos simplificar operações complexas envolvendo \(A\) ao operar diretamente sobre a matriz diagonal \(\Lambda\), facilitando cálculos como potências de \(A\) em aprendizado de máquina, especialmente na Análise de Componentes Principais (PCA), onde a diagonalização ajuda a encontrar direções principais de variação nos dados.

---

## 5. Decomposição em Valores Singulares (SVD) e Transformação de Bases

### Decomposição de Valores Singulares (SVD)
   - **Definição**: A SVD expressa uma matriz \(A\) como \( A = U \Sigma V^T \), onde \(U\) e \(V\) são ortogonais e \(\Sigma\) é uma matriz diagonal com valores singulares.
   - **Cálculo dos Valores Singulares**: Os valores singulares de \(A\) são as raízes quadradas dos autovalores de \(A^T A\).

### Exemplo Real e Cenário de Prova

- **Exemplo Real**: Em sistemas de recomendação, a SVD pode decompor uma matriz de classificações, ajudando a identificar padrões latentes entre usuários e itens (filmes, por exemplo). Suponha a matriz \( A \) que representa as classificações de usuários para filmes:
  \[
  A = \begin{bmatrix} 4 & 0 \\ 3 & -5 \end{bmatrix}
  \]
  Para aplicar SVD, vamos decompor \( A \) como \( A = U \Sigma V^T \), onde:
  - \( U \): matriz cujas colunas são os autovetores de \( A A^T \)
  - \( V \): matriz cujas colunas são os autovetores de \( A^T A \)
  - \( \Sigma \): matriz diagonal contendo os valores singulares (raízes quadradas dos autovalores de \( A^T A \))

#### Passo a Passo para Calcular a SVD de \( A \)

1. **Calcular \( A^T A \)** e encontrar seus autovalores para determinar \( V \) e \( \Sigma \):
   \[
   A^T = \begin{bmatrix} 4 & 3 \\ 0 & -5 \end{bmatrix}
   \]
   \[
   A^T A = \begin{bmatrix} 4 & 3 \\ 0 & -5 \end{bmatrix} \begin{bmatrix} 4 & 0 \\ 3 & -5 \end{bmatrix} = \begin{bmatrix} 16 & 0 \\ 0 & 25 \end{bmatrix}
   \]
   - Os autovalores de \( A^T A \) são \( 25 \) e \( 9 \), portanto, os valores singulares de \( A \) são \( \sigma_1 = 5 \) e \( \sigma_2 = 3 \), que compõem a matriz \( \Sigma \):
     \[
     \Sigma = \begin{bmatrix} 5 & 0 \\ 0 & 3 \end{bmatrix}
     \]

2. **Calcular os Autovetores de \( A^T A \) para Determinar \( V \)**:
   - Os autovetores associados aos autovalores \(25\) e \(9\) são respectivamente \(\vec{v}_1 = \begin{bmatrix} 0.6 \\ 0.8 \end{bmatrix}\) e \(\vec{v}_2 = \begin{bmatrix} -0.8 \\ 0.6 \end{bmatrix}\), que formam a matriz \( V \):
     \[
     V = \begin{bmatrix} 0.6 & -0.8 \\ 0.8 & 0.6 \end{bmatrix}
     \]

3. **Calcular \( A A^T \) e seus Autovetores para Determinar \( U \)**:
   - Calculando \( A A^T \):
     \[
     A A^T = \begin{bmatrix} 4 & 0 \\ 3 & -5 \end{bmatrix} \begin{bmatrix} 4 & 3 \\ 0 & -5 \end{bmatrix} = \begin{bmatrix} 16 & 15 \\ 15 & 34 \end{bmatrix}
     \]
   - Os autovetores de \( A A^T \) correspondem aos valores singulares, então encontramos \(\vec{u}_1 = \begin{bmatrix} 0.8 \\ 0.6 \end{bmatrix}\) e \(\vec{u}_2 = \begin{bmatrix} 0.6 \\ -0.8 \end{bmatrix}\), formando a matriz \( U \):
     \[
     U = \begin{bmatrix} 0.8 & 0.6 \\ 0.6 & -0.8 \end{bmatrix}
     \]

4. **Montando a Decomposição SVD Completa**:
   - A decomposição \( A = U \Sigma V^T \) é:
     \[
     A = \begin{bmatrix} 0.8 & 0.6 \\ 0.6 & -0.8 \end{bmatrix} \begin{bmatrix} 5 & 0 \\ 0 & 3 \end{bmatrix} \begin{bmatrix} 0.6 & -0.8 \\ 0.8 & 0.6 \end{bmatrix}
     \]

5. **Interpretação**:
   - Os valores singulares \(5\) e \(3\) representam as importâncias relativas das duas "dimensões principais" dos dados. Em um sistema de recomendação, essas dimensões podem capturar padrões como preferências de gênero ou outros fatores latentes, ajudando a recomendar itens que se alinhem com o perfil de preferências dos usuários.

### Cenário de Prova
O enunciado poderia pedir ao aluno para calcular a SVD de uma matriz de dados e interpretar como cada valor singular revela informações latentes dos dados, importantes para personalizar recomendações. A resposta envolveria calcular as matrizes \( U \), \( \Sigma \) e \( V \) e explicar como a decomposição ajuda a identificar padrões subjacentes em sistemas de recomendação.

### O Que é a Decomposição em Valores Singulares (SVD)?

A **Decomposição em Valores Singulares** de uma matriz \( A \) permite "quebrar" essa matriz em três partes principais: duas matrizes de rotação (\( U \) e \( V^T \)) e uma matriz diagonal (\( \Sigma \)), que contém valores chamados **valores singulares**. O SVD é uma ferramenta poderosa, especialmente em áreas como compressão de dados, análise de imagens e recomendação, pois ajuda a simplificar a estrutura dos dados e encontrar direções principais de variação.

Em termos matemáticos, dado uma matriz \( A \) (de dimensão \( m \times n \)), a decomposição SVD permite escrevê-la da seguinte forma:
\[
A = U \Sigma V^T
\]
onde:
- \( U \) é uma matriz ortogonal de dimensão \( m \times m \) (contém autovetores de \( A A^T \)),
- \( \Sigma \) é uma matriz diagonal \( m \times n \), contendo os **valores singulares**,
- \( V^T \) é a transposta de uma matriz ortogonal \( n \times n \) (contém autovetores de \( A^T A \)).

Vamos agora ao passo a passo de como calcular a SVD.

---

### Passo 1: Calcular \( A^T A \) e Seus Autovalores e Autovetores

1. Primeiro, calculamos a **matriz transposta** de \( A \), chamada \( A^T \), e multiplicamos \( A^T \) por \( A \):
   \[
   A^T A
   \]
   O objetivo de calcular \( A^T A \) é encontrar seus autovalores, que nos darão os **valores singulares** de \( A \).

2. Em seguida, calculamos os **autovalores** de \( A^T A \). Esses autovalores, após serem convertidos em raízes quadradas, vão para a matriz diagonal \( \Sigma \) como os valores singulares de \( A \).

3. **Autovetores** de \( A^T A \) formam as colunas da matriz \( V \), que é a matriz associada às direções dos dados.

### Passo 2: Formar a Matriz \( \Sigma \) com os Valores Singulares

1. **Valores Singulares**: São as raízes quadradas dos autovalores encontrados no passo 1. Por exemplo, se os autovalores de \( A^T A \) forem 25 e 9, os valores singulares de \( A \) serão 5 e 3 (a raiz quadrada de cada autovalor).
   
2. Esses valores singulares são organizados na matriz \( \Sigma \), que é uma **matriz diagonal** onde cada valor singular está em uma posição diagonal:
   \[
   \Sigma = \begin{bmatrix} 5 & 0 \\ 0 & 3 \end{bmatrix}
   \]

### Passo 3: Calcular \( A A^T \) e Seus Autovetores para Formar a Matriz \( U \)

1. Agora, calculamos a matriz \( A A^T \), que é o produto de \( A \) com sua transposta:
   \[
   A A^T
   \]
   Os autovetores de \( A A^T \) formam as colunas da matriz \( U \), que representa as direções principais dos dados originais \( A \).

2. Assim, obtemos a matriz \( U \) usando os autovetores de \( A A^T \).

### Passo 4: Montar a Decomposição SVD

Agora que temos \( U \), \( \Sigma \) e \( V \), a decomposição SVD completa de \( A \) é:
\[
A = U \Sigma V^T
\]

### Exemplo Prático

Vamos usar uma matriz simples para ilustrar esse processo. Considere a matriz:
\[
A = \begin{bmatrix} 4 & 0 \\ 3 & -5 \end{bmatrix}
\]

1. **Calcule \( A^T A \)**:
   \[
   A^T = \begin{bmatrix} 4 & 3 \\ 0 & -5 \end{bmatrix}
   \]
   \[
   A^T A = \begin{bmatrix} 4 & 3 \\ 0 & -5 \end{bmatrix} \begin{bmatrix} 4 & 0 \\ 3 & -5 \end{bmatrix} = \begin{bmatrix} 16 & 0 \\ 0 & 25 \end{bmatrix}
   \]

2. **Encontre os Autovalores de \( A^T A \)**:
   - Os autovalores são 25 e 9, então os valores singulares são \( \sqrt{25} = 5 \) e \( \sqrt{9} = 3 \).

3. **Forme a Matriz \( \Sigma \)**:
   \[
   \Sigma = \begin{bmatrix} 5 & 0 \\ 0 & 3 \end{bmatrix}
   \]

4. **Calcule os Autovetores de \( A^T A \) para Encontrar \( V \)**:
   - Os autovetores de \( A^T A \) são \(\begin{bmatrix} 0.6 \\ 0.8 \end{bmatrix}\) e \(\begin{bmatrix} -0.8 \\ 0.6 \end{bmatrix}\), formando a matriz \( V \):
     \[
     V = \begin{bmatrix} 0.6 & -0.8 \\ 0.8 & 0.6 \end{bmatrix}
     \]

5. **Calcule \( A A^T \) para Encontrar \( U \)**:
   \[
   A A^T = \begin{bmatrix} 4 & 0 \\ 3 & -5 \end{bmatrix} \begin{bmatrix} 4 & 3 \\ 0 & -5 \end{bmatrix} = \begin{bmatrix} 16 & 15 \\ 15 & 34 \end{bmatrix}
   \]
   - Os autovetores são \(\begin{bmatrix} 0.8 \\ 0.6 \end{bmatrix}\) e \(\begin{bmatrix} 0.6 \\ -0.8 \end{bmatrix}\), formando \( U \):
     \[
     U = \begin{bmatrix} 0.8 & 0.6 \\ 0.6 & -0.8 \end{bmatrix}
     \]

6. **SVD Completa**:
   \[
   A = U \Sigma V^T = \begin{bmatrix} 0.8 & 0.6 \\ 0.6 & -0.8 \end{bmatrix} \begin{bmatrix} 5 & 0 \\ 0 & 3 \end{bmatrix} \begin{bmatrix} 0.6 & -0.8 \\ 0.8 & 0.6 \end{bmatrix}
   \]

---

### Interpretação dos Valores Singulares

Os valores singulares \(5\) e \(3\) capturam as direções principais dos dados em \( A \). Em sistemas de recomendação, por exemplo, esses valores singulares podem representar características dominantes, como preferências de gênero em filmes, ajudando a entender quais aspectos são mais relevantes para os usuários. 

Esse é o processo passo a passo da decomposição em valores singulares (SVD), incluindo os cálculos e as interpretações das partes \( U \), \( \Sigma \) e \( V \).


Aqui está um roteiro de estudos organizado para suas revisões de Álgebra Linear, com leitura, exercícios e referências de respostas.

---
# Exercícios

### **1. Vetores e Operações**
- **Objetivo:** Revisar conceitos de vetores e suas operações.
- **Leitura:** 
  - Seção 1.1 (pág. 3 à 16)
  - Seção 1.2 (pág. 18 à 28)
  - Livro: *POOLE, David. Álgebra linear: uma introdução moderna. 2. ed. São Paulo: Cengage Learning, 2016*.
- **Exercícios:** 
  - Seção 1.1: pág. 16 e 17 - exercícios 5, 19 e 25.
  - Seção 1.2: pág. 29 - exercícios 3, 19 e 39.
- **Respostas:** Páginas RESP1, RESP2 e RESP3.

---

### **2. Matrizes e Operações**
- **Objetivo:** Revisar conceitos de matrizes e suas operações.
- **Leitura:** 
  - Seção 3.1 (pág. 138 à 152)
  - Seção 3.2 (pág. 154 à 161)
  - Seção 3.3 (pág. 163 à 178)
  - Livro: *POOLE, David. Álgebra linear: uma introdução moderna. 2. ed. São Paulo: Cengage Learning, 2016*.
- **Exercícios:** 
  - Seção 3.1: pág. 152 e 153 - exercícios 7, 13 e 21.
  - Seção 3.2: pág. 161 e 163 - exercícios 5, 15 e 25.
  - Seção 3.3: pág. 178 e 179 - exercícios 7, 25 e 37.
- **Respostas:** Páginas RESP10 e RESP11.

---

### **3. Autovalores e Autovetores**
- **Objetivo:** Revisar conceitos de autovalores e autovetores.
- **Leitura:** 
  - Seção 4.1 (pág. 254 à 260)
  - Livro: *POOLE, David. Álgebra linear: uma introdução moderna. 2. ed. São Paulo: Cengage Learning, 2016*.
- **Exercícios:** 
  - Seção 4.1: pág. 260 e 261 - exercícios 3, 9 e 11.
- **Respostas:** Páginas RESP15 e RESP16.

---

### **4. Diagonalização de Matrizes**
- **Objetivo:** Estudar o procedimento para diagonalização de matrizes.
- **Leitura:** 
  - Seção 4.4 (pág. 301 à 309)
  - Livro: *POOLE, David. Álgebra linear: uma introdução moderna. 2. ed. São Paulo: Cengage Learning, 2016*.
- **Exercícios:** 
  - Seção 4.4: pág. 309 e 310 - exercícios 5, 9 e 13.
- **Respostas:** Página RESP17.

---

### **5. Decomposição de Matrizes (LU e SVD)**
- **Objetivo:** Revisar conceitos de decomposição de matrizes com foco em fatoração LU e SVD.
- **Leitura:** 
  - Seção 3.4 (pág. 180 à 189)
  - Seção 7.4 (pág. 590 à 608)
  - Livro: *POOLE, David. Álgebra linear: uma introdução moderna. 2. ed. São Paulo: Cengage Learning, 2016*.
- **Exercícios:** 
  - Seção 3.4: pág. 189 e 190 - exercícios 1, 3 e 27.
  - Seção 7.4: pág. 609 - exercícios 3 e 13.
- **Respostas:** Páginas RESP12 e RESP33.

---

### **6. Espaços Vetoriais, Base e Dimensão**
- **Objetivo:** Revisar conceitos de espaços vetoriais, base, dimensão e mudanças de base.
- **Leitura:** 
  - Seção 6.1 (pág. 429 à 441)
  - Seção 6.2 (pág. 443 à 456)
  - Seção 6.3 (pág. 463 à 470)
  - Livro: *POOLE, David. Álgebra linear: uma introdução moderna. 2. ed. São Paulo: Cengage Learning, 2016*.
- **Exercícios:** 
  - Seção 6.3: pág. 471 e 472 - exercícios 1, 3, 11 e 15.
- **Respostas:** Páginas RESP28 e RESP29.