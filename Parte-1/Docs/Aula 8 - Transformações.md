# Transformações Lineares

As transformações lineares são fundamentais em álgebra linear e possuem várias aplicações na computação, como gráficos 3D, compressão de imagem e machine learning. Em termos simples, uma transformação linear preserva operações de adição e multiplicação por escalar. Para entender melhor, vamos detalhar exemplos específicos de transformações lineares.

## Definição de Transformação Linear

Uma transformação linear \( T \) em um espaço vetorial é uma função que leva um vetor a outro, obedecendo às propriedades:
1. **Propriedade de adição**: \( T(v + u) = T(v) + T(u) \)
2. **Propriedade de multiplicação por escalar**: \( T(cv) = cT(v) \)

Exemplo de transformação linear:
\[
T(x, y, z) = (2x, y - z)
\]

Essa transformação aplica uma operação que multiplica \( x \) por 2 e subtrai \( z \) de \( y \).

## Multiplicação de Vetor por Escalar

Dada uma transformação \( T \), multiplicamos o vetor por uma constante:

\[
T(v) = av
\]

Para um vetor \( v = (x, y) \):
\[
2T(v) = 2(x, y) = (2x, 2y)
\]

Esse conceito é frequentemente usado para aplicar uma transformação escalada a um vetor, essencial em computação gráfica para escalonamento.

## Reflexões

Reflexões também são transformações lineares. A reflexão inverte o sinal de uma ou mais componentes do vetor, dependendo do quadrante.

Para um vetor \( v = (x, y) \):
\[
T(v) = (x, -y)
\]

Isso significa que a imagem do vetor, que inicialmente está no primeiro quadrante, se move para o quarto quadrante.

**Outros exemplos de reflexões:**
1. Reflexão no segundo quadrante: \((-x, y)\)
2. Reflexão no terceiro quadrante: \((-x, -y)\)

## Matriz de Transformação

A transformação linear pode ser expressa como uma multiplicação de matrizes, permitindo operações eficientes em sistemas computacionais. Dada \( T(x, y) = (-x, y) \), queremos encontrar a matriz que representa \( T \).

A matriz \( A \) para essa transformação é:
\[
A = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}
\]

Para aplicar \( T \) em \( v = \begin{pmatrix} 1 \\ 2 \end{pmatrix} \):
\[
A \cdot v = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ 2 \end{pmatrix} = \begin{pmatrix} -1 \\ 2 \end{pmatrix}
\]

## Bases do Sistema

Para representar transformações no plano, utilizamos uma base ortonormal (tipicamente \( \mathbf{i} \) e \( \mathbf{j} \) no plano cartesiano).

\[
v_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \mathbf{i}, \quad v_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \mathbf{j}
\]

A partir desses vetores, qualquer vetor no plano pode ser representado como uma combinação linear de \( v_1 \) e \( v_2 \), o que facilita as transformações em sistemas de coordenadas.

## Exemplo

Vamos considerar uma transformação linear \( T : \mathbb{R}^2 \rightarrow \mathbb{R}^3 \) que mapeia vetores de duas dimensões para vetores de três dimensões. A transformação \( T \) é definida pela multiplicação de uma matriz \( A \) com um vetor em \( \mathbb{R}^2 \).

\[
T(1,0) = (2,3,4)
\]
\[
T(0,1) = (5,5,5)
\]

A matriz de transformação será:
\[
A = \begin{pmatrix} 2 & 5 \\ 3 & 5 \\ 4 & 5 \end{pmatrix}
\]

Essa matriz \( A \) possui dimensão \( 3 \times 2 \), o que permite mapear vetores bidimensionais para vetores tridimensionais.

### Exemplo de Cálculo da Transformação

1. **Para o vetor \( (1, 0) \):**
   \[
   T(1, 0) = \begin{pmatrix} 2 & 5 \\ 3 & 5 \\ 4 & 5 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 2 \\ 3 \\ 4 \end{pmatrix}
   \]
   Portanto, \( T(1, 0) = (2, 3, 4) \).

2. **Para o vetor \( (0, 1) \):**
   \[
   T(0, 1) = \begin{pmatrix} 2 & 5 \\ 3 & 5 \\ 4 & 5 \end{pmatrix} \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 5 \\ 5 \\ 5 \end{pmatrix}
   \]
   Logo, \( T(0, 1) = (5, 5, 5) \).

Esses valores nos mostram como a transformação \( T \) atua nos vetores base de \( \mathbb{R}^2 \).

### Cálculo para um Vetor Arbitrário

Para um vetor qualquer, como \( (2, 3) \), podemos aplicar a mesma matriz para encontrar a transformação:

\[
T(2, 3) = \begin{pmatrix} 2 & 5 \\ 3 & 5 \\ 4 & 5 \end{pmatrix} \begin{pmatrix} 2 \\ 3 \end{pmatrix} = \begin{pmatrix} 19 \\ 21 \\ 23 \end{pmatrix}
\]

Portanto, \( T(2, 3) = (19, 21, 23) \).

### Generalização

Para uma transformação linear \( T \) que mapeia vetores de \( \mathbb{R}^m \) para \( \mathbb{R}^n \), a matriz \( A \) terá dimensão \( n \times m \), onde cada elemento da matriz controla como as componentes dos vetores de \( \mathbb{R}^m \) contribuem para as componentes resultantes em \( \mathbb{R}^n \).

# Matriz de Transformação para Rotação

A matriz de rotação é usada para rotacionar vetores em um plano bidimensional, mantendo a distância do vetor à origem, ou seja, preservando seu comprimento (norma). Ela é muito útil em computação gráfica, física e outras áreas que envolvem manipulação de vetores.

A matriz para uma rotação no plano em um ângulo \( \theta \) é dada por:

\[
\begin{pmatrix} \cos(\theta) & -\sin(\theta) \\ \sin(\theta) & \cos(\theta) \end{pmatrix}
\]

### Como a Matriz de Rotação Funciona

Para rotacionar um vetor \( v = (x, y) \) em torno da origem por um ângulo \( \theta \), multiplicamos o vetor pela matriz de rotação:

\[
\begin{pmatrix} \cos(\theta) & -\sin(\theta) \\ \sin(\theta) & \cos(\theta) \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x \cos(\theta) - y \sin(\theta) \\ x \sin(\theta) + y \cos(\theta) \end{pmatrix}
\]

Isso resulta em um novo vetor \( (x', y') \), que é o vetor \( v \) rotacionado de \( \theta \) graus no sentido anti-horário.

### Exemplo de Rotação

Para um vetor \( v = (1, 0) \) e um ângulo de rotação \( \theta = 90^\circ \):

1. \( \cos(90^\circ) = 0 \) e \( \sin(90^\circ) = 1 \).
2. A matriz de rotação se torna:
   \[
   \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}
   \]

Multiplicando pela matriz:

\[
\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}
\]

Portanto, rotacionar \( (1, 0) \) em \( 90^\circ \) resulta em \( (0, 1) \).

### Aplicações da Matriz de Rotação

A matriz de rotação é amplamente utilizada em:
- **Computação Gráfica**: Para rotacionar imagens, objetos 3D, etc.
- **Animações**: Para criar movimentos circulares ou girar elementos.
- **Física**: Para calcular rotações em planos e modelar movimentos circulares.

### Propriedades Importantes

- **Conservação da Norma**: A matriz de rotação não altera o comprimento do vetor.
- **Transformação Linear**: A rotação é uma transformação linear, pois preserva a adição de vetores e a multiplicação por escalar.

## Conclusão

As transformações lineares são úteis para manipular e modificar gráficos e estruturas de dados em computação. A representação matricial facilita a implementação de algoritmos eficientes, fundamentais para aplicações em computação gráfica e aprendizado de máquina. 