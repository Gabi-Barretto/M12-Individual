---------------------------------------------------
- Anotações sobre a prova

   - 4 ex de análise Léxica 2 easy 1 mid 1 hard
   - 2 ex de tipos de análise
   - 2 ex de gramáticas e BNF
   - Dissertativa
   - Uma é consequencia da outra
   - Usar o Algoritmo de Thompson para a análise léxica
---------------------------------------------------

# Análise Semântica

Análisa o funcionamento do código como um todo.

- Léxico é super leve, já esta rodando quando estamos codando. (Palavra isoladamente)

- O sintático é se a linha faz sentido, escopo maior.

- O semantico leva um pocuo mais tempo e olha o projeto como um todo, o contexto como um todo, erro e seus efeitos colaterais.
    - Checagem de tipos
    - Checagem de atributos
    - Análise de fluxo de controle

Analise semantica avalia se o código faz sentido de acordo com regras de linguagem de programação.

Busca garantir que o programa é coerente e consistente em temos de significado e lógica. 

✓ **Verificar a coerência semântica do código:** verificar se o código está de acordo com as regras da linguagem em relação a tipos de dados, escopo de variáveis, operações válidas, etc.

✓ **Detectar erros semânticos:** identificar problemas como variáveis não declaradas, tipos incompatíveis em operações, uso de funções inválidas, etc.

✓ **Preparar o código para a geração de código intermediário:** a análise semântica fornece informações essenciais para a etapa seguinte do processo de compilação, que é a geração de código.

### Escopo de variáveis

Tipos: Global, local, bloco.
Regras de visibilidade e acesso a variáveis.
Resolução de nomes e ambiguidades.
Exemplos de erros relacionados ao escopo cde variávies (ex.: vaiáveis não decladas, variável com nome já utilizado em outro escopo).

### Checagem de tipo

Tipos: estática e dinâmica.
Métodos de checagem: atribuição, operações aritméticas, comparações.
Exemplos de erros relacionados a checagem de tipos: tipos incompatíveis em uma atribuição, operação com tipos inválidos. 


"A" + "B" + "C" (concatenação) é menos eficiente que utilizar o *append*.

A alocação de memória acaba sendo menos eficiente, precisando de um novo espaço para cada etapa da concatenação.

### Tabela de simbolos

Informações armazenadas na tabela de símbolos (ex.: nome, tipo, escopo, endereço).
Utilização da tabela de símbolos durante a análise semântica.
Exemplos de como a tabela de símbolos é utilizada na checagem de tipos e resolução de nomes.

### Análise fluxo de controle 

Verificação de erros relacionados ao fluxo de controle.
Análise de laços e condições (ex.: loops infinitos, condições sem sentido).
Verificação de alcançabilidade de código.
Exemplos de erros relacionados ao fluxo de controle (ex.: variável utilizada antes de ser definida, código 
inalcançável).

### Checagem de Atribuitos

O que são atributos?
Checagem de atributos em declarações e usos.
Exemplos de atributos (ex.: tamanho de arrays, visibilidade de membros de classes).
Exemplos de erros relacionados a atributos (ex.: acesso a atributo inválido, tamanho de array inválido).

### Geração de Código Intermediário

O papel da análise semântica na geração de código intermediário.
Conversão de código fonte para código intermediário.
Exemplos de código intermediário (ex.: três endereços, código de máquina).

